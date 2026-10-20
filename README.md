# toad-bot-kit

A fan-made toolkit for **TOAD** (The Toad Pepe, a Solana memecoin, https://thetoadmeme.com/). It holds everything a Grok Bot TOAD X bot needs on first run: the brand kit, image and caption scripts, a publish ledger, and the template skills.

Not affiliated with or endorsed by the TOAD project. The official account is [@thetoadmeme_](https://x.com/thetoadmeme_).

## Install

New bots download the kit on first run into `TOAD_KIT=/home/box/shared/toad-kit`:

```bash
git clone --depth 1 https://github.com/grendizerwin/toadbot.git /home/box/shared/toad-kit      # or: git -C /home/box/shared/toad-kit pull
pip install --user -r /home/box/shared/toad-kit/requirements.txt   # Pillow
```

## Layout

```
bin/
  xai_image.py        xAI (Grok Imagine) image generate/edit CLI, stdlib only
  compose.py          Paper Pulse caption card (Pillow)
  toad_ledger.py      append-only JSONL publish ledger
kit/
  BRAND.md            brand reference (source of truth)
  prompt-kit.md       character lock, face check, prompt templates, voice cheat sheet
  assets/
    characters/       official character references and cutouts
    creator-kit/      official creator kit (zip + loose files)
    fonts/            Anton, Caveat, DM Sans, IBM Plex Mono (+ LICENSE, OFL-1.1)
    backgrounds/  brand-boards/  logos/  social/  video/
    paper-pulse-reference.png
  raw/                capture of thetoadmeme.com pages and CSS (reference only)
docs/
  skills/             template skills, one .md per skill
  references/         deeper playbooks (voice, hooks, visual bible, scoring, queries)
requirements.txt      Pillow
```

Community Meme Depot images aren't included (unclear reuse rights); see https://memedepot.com/d/the-toad-pepe.

## Requirements

- Python 3
- Pillow, for `compose.py` and caption work (`pip install -r requirements.txt`)
- ffmpeg, optional, for video captions

## Scripts

### bin/xai_image.py

Generates or edits images with xAI Grok Imagine and saves real files. Needs `XAI_API_KEY`. The key is never printed. Each image is billed to the key owner's xAI account.

```bash
# text to image
python3 bin/xai_image.py --prompt "..." --aspect-ratio 1:1 --out /home/box/shared/toad-media/2026-01-01-scene.jpg

# edit / compose with 1-5 references (switches to /v1/images/edits)
python3 bin/xai_image.py \
  --ref "$TOAD_KIT/kit/assets/characters/toad-front-reference-fullbody.jpg" \
  --ref "$TOAD_KIT/kit/assets/characters/toad-face-reference-circle.jpg" \
  --prompt "<character lock from kit/prompt-kit.md>. Only change: ..." --n 1
```

Options: `--prompt` (required), `--out` (absolute path; default is a timestamped file in `$TOAD_MEDIA_DIR`), `--ref` (repeatable, up to 5), `--n` (1-10), `--aspect-ratio`, `--resolution` (1k/1.5k/2k), `--quality`, `--model` (default grok-imagine-image-2.0), `--timeout`. Run `--help` for the full list.

### bin/compose.py

Renders a Paper Pulse card: cream paper with grain, Anton headline with a yellow brush underline, your photo, a Caveat note, and Plex Mono labels. Fonts load from `../kit/assets/fonts/`, so keep the folder layout.

```bash
python3 bin/compose.py <photo> <out.jpg> "<HEADLINE>" "<caveat note>" "<LEFT LABEL>" "<RIGHT LABEL>"
python3 bin/compose.py kit/assets/characters/toad-portrait-bust-green-bg.png /tmp/card.jpg \
  "TOAD IS HAVING A DAY." "same toad. different days." "MONDAY" "SOLANA"
```

### bin/toad_ledger.py

An append-only JSONL log of posts that went live, used to look back at what worked.

```bash
# record one verified live post
python3 bin/toad_ledger.py append --id 1234567890 --format orig-img --text "..." [--target @handle --target-followers N --slot 19:30 --draft "Jan 1 post 1"]
# entries from the last 72 h, or just their ids for get_posts_by_ids
python3 bin/toad_ledger.py recent --hours 72
python3 bin/toad_ledger.py recent --hours 72 --ids
```

`--format` is one of `orig-img`, `orig-card`, `orig-text`, `video`, `remix-reply`, `text-reply`. `--ledger PATH` overrides the default file. Row URLs are `https://x.com/i/status/<id>`, or `https://x.com/<X_HANDLE>/status/<id>` when `X_HANDLE` is set.

## Environment variables

| Variable | Used by | Default |
|---|---|---|
| `XAI_API_KEY` | `xai_image.py` | required for image generation; never commit it |
| `TOAD_MEDIA_DIR` | `xai_image.py` default output folder | `/home/box/shared/toad-media` |
| `TOAD_STATE_DIR` | `toad_ledger.py` default ledger folder (`toad-ledger.jsonl`) | `/home/box/shared/toad-state` |
| `X_HANDLE` | `toad_ledger.py` (optional, for row URLs) | unset, so URLs use `x.com/i/status/<id>` |

## Ground rules for bots using this kit

Write as a pond member, not as the project. No price talk, no invented news, no wallets or holdings, and nothing posts without the owner's approval of the exact draft. The skills in `docs/skills/` spell this out.
