#!/usr/bin/env python3
"""Archive superseded Codex automation-run sessions through the supported CLI."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
from collections import defaultdict
from pathlib import Path


AUTOMATION_ID_RE = re.compile(r"^Automation ID:\s*(\S+)\s*$", re.MULTILINE)


def configured_ids(codex_home: Path) -> set[str]:
    ids: set[str] = set()
    for path in (codex_home / "automations").glob("*/automation.toml"):
        text = path.read_text(encoding="utf-8")
        match = re.search(r'^id\s*=\s*"([^"]+)"', text, re.MULTILINE)
        status = re.search(r'^status\s*=\s*"([^"]+)"', text, re.MULTILINE)
        if match and (not status or status.group(1).upper() == "ACTIVE"):
            ids.add(match.group(1))
    return ids


def state_db(codex_home: Path) -> Path:
    candidates = sorted(codex_home.glob("state_*.sqlite"), key=lambda path: path.stat().st_mtime, reverse=True)
    if not candidates:
        raise FileNotFoundError(f"No state_*.sqlite found under {codex_home}")
    return candidates[0]


def active_automation_runs(db_path: Path, automation_ids: set[str]) -> list[dict[str, object]]:
    connection = sqlite3.connect(f"file:{db_path.as_posix()}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute(
            """
            SELECT id, title, created_at
            FROM threads
            WHERE archived = 0
              AND thread_source = 'automation'
              AND title LIKE 'Automation:%'
            ORDER BY created_at DESC, id DESC
            """
        ).fetchall()
    finally:
        connection.close()

    result: list[dict[str, object]] = []
    for row in rows:
        match = AUTOMATION_ID_RE.search(row["title"])
        if match and match.group(1) in automation_ids:
            result.append(
                {
                    "id": row["id"],
                    "automation_id": match.group(1),
                    "created_at": row["created_at"],
                    "title": row["title"].splitlines()[0],
                }
            )
    return result


def retention_plan(rows: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row["automation_id"])].append(row)

    keep: list[dict[str, object]] = []
    archive: list[dict[str, object]] = []
    for automation_id in sorted(grouped):
        ordered = sorted(grouped[automation_id], key=lambda row: (int(row["created_at"]), str(row["id"])), reverse=True)
        keep.extend(ordered[:1])
        archive.extend(ordered[1:])
    return keep, archive


def codex_cli() -> Path:
    local_app_data = Path(os.environ.get("LOCALAPPDATA", ""))
    candidates = sorted(
        (local_app_data / "OpenAI" / "Codex" / "bin").glob("*/codex.exe"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    if candidates:
        return candidates[0]
    on_path = shutil.which("codex")
    if on_path:
        return Path(on_path)
    raise FileNotFoundError("codex executable was not found")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Archive planned sessions; default is dry-run.")
    parser.add_argument("--codex-home", type=Path, default=Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex"))
    args = parser.parse_args()

    ids = configured_ids(args.codex_home)
    db_path = state_db(args.codex_home)
    before = active_automation_runs(db_path, ids)
    keep, archive = retention_plan(before)
    failures: list[dict[str, str]] = []
    archived_ids: list[str] = []

    if args.apply and archive:
        executable = codex_cli()
        for row in archive:
            session_id = str(row["id"])
            process = subprocess.run(
                [str(executable), "archive", session_id],
                check=False,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            if process.returncode == 0:
                archived_ids.append(session_id)
            else:
                failures.append(
                    {
                        "id": session_id,
                        "error": (process.stderr or process.stdout).strip(),
                    }
                )

    after = active_automation_runs(db_path, ids)
    remaining_counts: dict[str, int] = defaultdict(int)
    for row in after:
        remaining_counts[str(row["automation_id"])] += 1

    report = {
        "mode": "apply" if args.apply else "dry-run",
        "configured_automation_ids": sorted(ids),
        "kept": keep,
        "planned_archive_ids": [str(row["id"]) for row in archive],
        "archived_ids": archived_ids,
        "failures": failures,
        "remaining_active_runs": dict(sorted(remaining_counts.items())),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if failures:
        return 1
    if args.apply and any(count > 1 for count in remaining_counts.values()):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
