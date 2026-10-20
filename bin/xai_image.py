#!/usr/bin/env python3
"""Box-local xAI (Grok Imagine) image generation/editing CLI. Stdlib only.

Saves real image files on the box so they can be uploaded to X via the browser.
Reads the API key from env XAI_API_KEY (never printed).

Text-to-image : POST https://api.x.ai/v1/images/generations
With --ref    : POST https://api.x.ai/v1/images/edits   (1-5 reference/source images)
"""
import argparse, base64, datetime, json, mimetypes, os, sys, urllib.error, urllib.request

API = "https://api.x.ai/v1"
DEFAULT_MODEL = "grok-imagine-image-2.0"
DEFAULT_DIR = os.environ.get("TOAD_MEDIA_DIR", "/home/box/shared/toad-media")
ASPECTS = ["1:1", "3:4", "4:3", "9:16", "16:9", "2:3", "3:2", "9:19.5", "19.5:9",
           "9:20", "20:9", "1:2", "2:1", "21:9", "5:2", "auto"]
EXT = {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp"}


def die(msg, code=1):
    key = os.environ.get("XAI_API_KEY")
    if key:
        msg = msg.replace(key, "[REDACTED]")
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def data_url(path):
    if not os.path.isfile(path):
        die(f"reference image not found: {path}")
    mime = mimetypes.guess_type(path)[0] or "image/jpeg"
    if mime not in EXT:
        die(f"reference must be JPEG, PNG or WebP (got {mime}): {path}")
    with open(path, "rb") as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"


def post(endpoint, payload, key, timeout):
    req = urllib.request.Request(
        f"{API}{endpoint}", data=json.dumps(payload).encode(), method="POST",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                 "User-Agent": "xai-image-cli/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:1500]
        die(f"API {endpoint} returned HTTP {e.code}: {body}")
    except urllib.error.URLError as e:
        die(f"network error calling {endpoint}: {e.reason}")
    except TimeoutError:
        die(f"timed out after {timeout}s calling {endpoint}")
    except json.JSONDecodeError:
        die(f"API {endpoint} returned non-JSON response")


def fetch(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": "xai-image-cli/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read(), r.headers.get_content_type()
    except Exception as e:
        die(f"failed to download generated image: {e}")


def sniff(b):
    if b[:3] == b"\xff\xd8\xff": return ".jpg"
    if b[:8] == b"\x89PNG\r\n\x1a\n": return ".png"
    if b[:4] == b"RIFF" and b[8:12] == b"WEBP": return ".webp"
    return None


def main():
    p = argparse.ArgumentParser(description="Generate or edit images with xAI Grok Imagine; saves files on the box.")
    p.add_argument("--prompt", required=True, help="Text prompt (with --ref: the edit/compose instruction; refer to refs as <IMAGE_0>, <IMAGE_1>...)")
    p.add_argument("--out", help=f"Absolute output path (e.g. {DEFAULT_DIR}/2026-01-01-scene.jpg). Default: timestamped file in $TOAD_MEDIA_DIR (currently {DEFAULT_DIR}/). With --n>1, -2, -3... are appended.")
    p.add_argument("--model", default=DEFAULT_MODEL, help=f"Model (default {DEFAULT_MODEL}; also grok-imagine-image, grok-imagine-image-quality)")
    p.add_argument("--n", type=int, default=1, help="Number of images (1-10, default 1)")
    p.add_argument("--aspect-ratio", choices=ASPECTS, help="Aspect ratio, e.g. 16:9, 1:1, 4:3 (default auto / follows first ref)")
    p.add_argument("--resolution", choices=["1k", "1.5k", "2k"], help="Output resolution (default server-chosen)")
    p.add_argument("--quality", choices=["low", "medium", "auto"], help="Quality (grok-imagine-image-2.0 only)")
    p.add_argument("--ref", action="append", default=[], help="Local reference/source image path (JPEG/PNG/WebP), repeatable up to 5. Switches to /v1/images/edits.")
    p.add_argument("--timeout", type=int, default=300, help="HTTP timeout seconds (default 300)")
    a = p.parse_args()

    key = os.environ.get("XAI_API_KEY")
    if not key:
        die("XAI_API_KEY is not set in the environment")
    if not 1 <= a.n <= 10:
        die("--n must be between 1 and 10")
    if len(a.ref) > 5:
        die("at most 5 --ref images are supported")
    if a.out and not os.path.isabs(a.out):
        die("--out must be an absolute path")

    payload = {"model": a.model, "prompt": a.prompt, "n": a.n, "response_format": "b64_json"}
    if a.aspect_ratio: payload["aspect_ratio"] = a.aspect_ratio
    if a.resolution: payload["resolution"] = a.resolution
    if a.quality: payload["quality"] = a.quality

    if a.ref:
        imgs = [{"url": data_url(r), "type": "image_url"} for r in a.ref]
        if len(imgs) == 1:
            payload["image"] = imgs[0]
        else:
            payload["images"] = imgs
        endpoint = "/images/edits"
    else:
        endpoint = "/images/generations"

    resp = post(endpoint, payload, key, a.timeout)
    if isinstance(resp, dict) and resp.get("error"):
        die(f"API error: {json.dumps(resp['error'])[:1500]}")
    data = (resp or {}).get("data") or []
    if not data:
        die(f"API returned no images: {json.dumps(resp)[:1500]}")

    if a.out:
        base, ext0 = os.path.splitext(a.out)
    else:
        ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        base, ext0 = os.path.join(DEFAULT_DIR, f"img-{ts}"), ""

    saved, revised = [], []
    for i, item in enumerate(data):
        if item.get("b64_json"):
            blob = base64.b64decode(item["b64_json"])
            mime = item.get("mime_type")
        elif item.get("url"):
            blob, mime = fetch(item["url"], a.timeout)
            mime = item.get("mime_type") or mime
        else:
            die(f"image {i} had neither b64_json nor url (storage_error={item.get('storage_error')})")
        ext = ext0 or sniff(blob) or EXT.get(mime or "", ".jpg")
        real = sniff(blob)
        if ext0 and real and real != ext0.lower() and not (real == ".jpg" and ext0.lower() == ".jpeg"):
            print(f"WARNING: image is {real} but --out ends in {ext0}; saving with requested name anyway", file=sys.stderr)
        path = f"{base}{'' if i == 0 else f'-{i+1}'}{ext}"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(blob)
        try: os.chmod(path, 0o666)
        except OSError: pass
        saved.append(os.path.abspath(path))
        if item.get("revised_prompt"):
            revised.append(item["revised_prompt"])

    for s in saved:
        print(s)
    if revised:
        for r in revised:
            print(f"REVISED_PROMPT: {r}")
    model_used = resp.get("model")
    if model_used:
        print(f"MODEL: {model_used}", file=sys.stderr)


if __name__ == "__main__":
    main()
