#!/usr/bin/env python3
"""Toad's publish ledger (one JSON object per line).

append: record one live post right after its read-tool verification.
recent: list entries from the last N hours; --ids prints a comma-separated id list
        ready for get_posts_by_ids (post.fields=public_metrics,created_at).
"""
import argparse, json, os, sys
from datetime import datetime, timedelta, timezone

STATE_DIR = os.environ.get("TOAD_STATE_DIR", "/home/box/shared/toad-state")
DEFAULT = os.path.join(STATE_DIR, "toad-ledger.jsonl")


def status_url(post_id):
    handle = os.environ.get("X_HANDLE", "").strip().lstrip("@")
    return f"https://x.com/{handle}/status/{post_id}" if handle else f"https://x.com/i/status/{post_id}"

FORMATS = ["orig-img", "orig-card", "orig-text", "video", "remix-reply", "text-reply"]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ledger", default=DEFAULT, help=f"ledger path (default: $TOAD_STATE_DIR/toad-ledger.jsonl = {DEFAULT})")
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("append")
    a.add_argument("--id", required=True, help="numeric status id")
    a.add_argument("--format", required=True, choices=FORMATS)
    a.add_argument("--text", default="")
    a.add_argument("--target", default="", help="@handle replied to (empty for originals)")
    a.add_argument("--target-followers", type=int)
    a.add_argument("--slot", default="", help="planned slot, e.g. 19:30")
    a.add_argument("--draft", default="", help="date-based draft label, e.g. 'Oct 20 post 2'")
    a.add_argument("--ts", help="posted time, ISO 8601 (default: now)")
    r = sub.add_parser("recent")
    r.add_argument("--hours", type=float, default=72)
    r.add_argument("--ids", action="store_true")
    args = ap.parse_args()

    if args.cmd == "append":
        if not args.id.isdigit():
            sys.exit("ERROR: --id must be the numeric status id")
        ts = args.ts or datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
        datetime.fromisoformat(ts)  # validate
        try:
            with open(args.ledger) as f:
                if any(json.loads(l).get("id") == args.id for l in f if l.strip()):
                    print(f"skip: {args.id} already in ledger"); return
        except FileNotFoundError:
            pass
        row = {"bot": "toad", "id": args.id, "url": status_url(args.id),
               "format": args.format, "text": args.text, "target": args.target.lstrip("@"),
               "target_followers": args.target_followers, "slot": args.slot, "draft": args.draft, "ts": ts}
        os.makedirs(os.path.dirname(os.path.abspath(args.ledger)), exist_ok=True)
        with open(args.ledger, "a") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"appended {args.id}")
        return

    cutoff = datetime.now(timezone.utc) - timedelta(hours=args.hours)
    rows = []
    try:
        with open(args.ledger) as f:
            for l in f:
                if l.strip():
                    o = json.loads(l)
                    if datetime.fromisoformat(o["ts"]) >= cutoff:
                        rows.append(o)
    except FileNotFoundError:
        pass
    if args.ids:
        print(",".join(o["id"] for o in rows))
    else:
        for o in rows:
            print(json.dumps(o, ensure_ascii=False))

if __name__ == "__main__":
    main()
