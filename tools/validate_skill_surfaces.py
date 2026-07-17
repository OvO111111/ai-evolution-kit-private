from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    values: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return values
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip("'\"")
    return {}


def direct_skills(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path.parent for path in root.glob("*/SKILL.md"))


def run_codex_validation(codex_home: Path) -> dict[str, Any]:
    skills = direct_skills(codex_home / "skills")
    validator = codex_home / "skills" / ".system" / "skill-creator" / "scripts" / "quick_validate.py"
    failures: list[dict[str, str]] = []
    if not validator.exists():
        return {
            "owner": "codex",
            "checked": len(skills),
            "passed": 0,
            "failures": [{"skill": "<validator>", "error": f"missing {validator}"}],
        }
    env = dict(os.environ)
    env["PYTHONUTF8"] = "1"
    for skill in skills:
        proc = subprocess.run(
            [sys.executable, str(validator), str(skill)],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,
        )
        if proc.returncode:
            failures.append({"skill": skill.name, "error": proc.stdout.strip()})
    return {
        "owner": "codex",
        "checked": len(skills),
        "passed": len(skills) - len(failures),
        "failures": failures,
    }


def extract_json(text: str) -> dict[str, Any]:
    start = text.find("{")
    if start < 0:
        raise ValueError("command returned no JSON object")
    value, _end = json.JSONDecoder().raw_decode(text[start:])
    if not isinstance(value, dict):
        raise ValueError("command JSON root is not an object")
    return value


def run_lark_check(agents_home: Path, skip_live: bool) -> dict[str, Any]:
    skills = direct_skills(agents_home / "skills")
    failures: list[dict[str, str]] = []
    names: set[str] = set()
    for skill in skills:
        meta = parse_frontmatter(skill / "SKILL.md")
        name = meta.get("name", "")
        if not name or not meta.get("description") or not meta.get("version"):
            failures.append({"skill": skill.name, "error": "missing name, description, or Lark-managed version"})
        elif name != skill.name:
            failures.append({"skill": skill.name, "error": f"frontmatter name is {name!r}"})
        names.add(name or skill.name)

    lock_path = agents_home / ".skill-lock.json"
    lock_names: set[str] = set()
    if not lock_path.exists():
        failures.append({"skill": "<lock>", "error": f"missing {lock_path}"})
    else:
        lock = json.loads(lock_path.read_text(encoding="utf-8-sig"))
        lock_names = set((lock.get("skills") or {}).keys())
        if names != lock_names:
            failures.append(
                {
                    "skill": "<lock>",
                    "error": f"directory/lock mismatch: missing={sorted(lock_names - names)}, extra={sorted(names - lock_names)}",
                }
            )

    live: dict[str, Any] = {"status": "skipped"}
    if not skip_live:
        if not shutil.which("lark-cli"):
            failures.append({"skill": "<lark-cli>", "error": "lark-cli is not on PATH"})
            live = {"status": "unavailable"}
        else:
            command = ["lark-cli", "update", "--check", "--json"]
            if os.name == "nt":
                command = ["cmd", "/d", "/c", *command]
            proc = subprocess.run(
                command,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=120,
            )
            try:
                payload = extract_json(proc.stdout)
                status = payload.get("skills_status") or {}
                live = {
                    "status": "checked",
                    "ok": payload.get("ok") is True,
                    "current_version": payload.get("current_version"),
                    "latest_version": payload.get("latest_version"),
                    "in_sync": status.get("in_sync"),
                    "official": status.get("official"),
                    "updated": status.get("updated"),
                }
                if (
                    proc.returncode
                    or payload.get("ok") is not True
                    or status.get("in_sync") is not True
                    or status.get("official") != len(skills)
                    or status.get("updated") != len(skills)
                ):
                    failures.append({"skill": "<lark-cli>", "error": f"live skills status mismatch: {live}"})
            except (json.JSONDecodeError, ValueError) as exc:
                live = {"status": "failed", "error": str(exc)}
                failures.append({"skill": "<lark-cli>", "error": str(exc)})

    return {
        "owner": "lark-cli",
        "checked": len(skills),
        "passed": len(skills) - sum(1 for item in failures if not item["skill"].startswith("<")),
        "lock_entries": len(lock_names),
        "live": live,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate active skills with the schema and live checks owned by each surface.")
    parser.add_argument("--codex-home", type=Path, default=Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex"))
    parser.add_argument("--agents-home", type=Path, default=Path.home() / ".agents")
    parser.add_argument("--skip-live", action="store_true")
    args = parser.parse_args()

    results = [run_codex_validation(args.codex_home), run_lark_check(args.agents_home, args.skip_live)]
    failures = [failure for result in results for failure in result["failures"]]
    report = {
        "surfaces": results,
        "total_checked": sum(result["checked"] for result in results),
        "failed_checks": len(failures),
        "ok": not failures,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
