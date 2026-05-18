#!/usr/bin/env python3
import argparse
import json
import os
import subprocess
import sys


WX = ["npx.cmd" if os.name == "nt" else "npx", "-y", "@jackwener/wx-cli"]


def run_wx(args):
    proc = subprocess.run(
        WX + args,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.strip() or proc.stdout.strip() or f"wx-cli failed: {proc.returncode}")
    return proc.stdout


def load_history(chat, limit, offset=0, since=None, until=None):
    args = ["history", chat, "-n", str(limit), "--offset", str(offset), "--type", "text", "--json"]
    if since:
        args += ["--since", since]
    if until:
        args += ["--until", until]
    raw = run_wx(args)
    return json.loads(raw)


def cmd_list(args):
    raw = run_wx(["sessions", "-n", str(args.limit), "--json"])
    if not raw.strip():
        raw = run_wx(["sessions", "-n", str(args.limit)])
        print(raw)
        return
    data = json.loads(raw)
    sessions = data.get("sessions", data if isinstance(data, list) else [])
    out = []
    for item in sessions:
        if args.groups_only and not item.get("is_group"):
            continue
        out.append({
            "chat": item.get("chat"),
            "chat_type": item.get("chat_type"),
            "is_group": item.get("is_group"),
            "time": item.get("time"),
            "unread": item.get("unread"),
            "username": item.get("username"),
        })
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_history(args):
    data = load_history(args.chat, args.limit, args.offset, args.since, args.until)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_search_local(args):
    data = load_history(args.chat, args.limit, 0, args.since, args.until)
    messages = data.get("messages", [])
    hits = []
    for msg in messages:
        content = msg.get("content") or ""
        if args.keyword in content:
            hits.append(msg)
    out = {
        "chat": data.get("chat", args.chat),
        "keyword": args.keyword,
        "source_count": len(messages),
        "hit_count": len(hits),
        "messages": hits,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Read local WeChat group context without sending messages.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("list")
    p.add_argument("--limit", type=int, default=30)
    p.add_argument("--groups-only", action="store_true")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("history")
    p.add_argument("--chat", required=True)
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--since")
    p.add_argument("--until")
    p.set_defaults(func=cmd_history)

    p = sub.add_parser("search-local")
    p.add_argument("--chat", required=True)
    p.add_argument("--keyword", required=True)
    p.add_argument("--limit", type=int, default=200)
    p.add_argument("--since")
    p.add_argument("--until")
    p.set_defaults(func=cmd_search_local)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    if sys.platform.startswith("win"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
