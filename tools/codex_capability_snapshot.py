from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def run(args: list[str], timeout: int = 20) -> tuple[int, str, str]:
    proc = subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()


def powershell(script: str, timeout: int = 20) -> str | None:
    code, out, _err = run(["powershell", "-NoProfile", "-Command", script], timeout=timeout)
    return out if code == 0 and out else None


def list_dir_names(path: Path) -> list[str]:
    if not path.exists():
        return []
    return sorted(item.name for item in path.iterdir() if item.is_dir())


def latest_semverish(values: list[str]) -> str | None:
    if not values:
        return None

    def key(value: str) -> tuple[int, int, int, str]:
        match = re.match(r"^v?(\d+)(?:\.(\d+))?(?:\.(\d+))?", value)
        if not match:
            return (-1, -1, -1, value)
        return (
            int(match.group(1) or 0),
            int(match.group(2) or 0),
            int(match.group(3) or 0),
            value,
        )

    return sorted(values, key=key)[-1]


def collect_codex_app() -> dict[str, Any]:
    source = powershell("(Get-Command codex -ErrorAction SilentlyContinue).Source")
    version = None
    if source:
        match = re.search(r"OpenAI\.Codex_([^\\/]+)", source)
        if match:
            version = match.group(1)
    return {"source": source, "package_version": version}


def collect_plugin_cache(codex_home: Path) -> dict[str, Any]:
    cache = codex_home / "plugins" / "cache"
    groups: dict[str, Any] = {}
    for group in ["openai-bundled", "openai-curated", "openai-curated-remote", "openai-primary-runtime"]:
        group_path = cache / group
        plugins: dict[str, Any] = {}
        if group_path.exists():
            for plugin_path in sorted(p for p in group_path.iterdir() if p.is_dir()):
                versions = list_dir_names(plugin_path)
                plugins[plugin_path.name] = {
                    "versions": versions,
                    "latest": latest_semverish(versions) or (versions[-1] if versions else None),
                }
        groups[group] = plugins
    return groups


def npm_outdated() -> dict[str, Any]:
    npm_command = shutil.which("npm") or shutil.which("npm.cmd") or shutil.which("npm.ps1")
    if not npm_command:
        return {"available": False}
    if npm_command.lower().endswith(".ps1"):
        command = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", npm_command, "outdated", "-g", "--depth=0", "--json"]
    else:
        command = [npm_command, "outdated", "-g", "--depth=0", "--json"]
    code, out, err = run(command, timeout=60)
    if not out:
        return {"available": True, "outdated": {}, "stderr": err, "exit_code": code}
    try:
        data = json.loads(out)
    except json.JSONDecodeError:
        return {"available": True, "parse_error": out, "stderr": err, "exit_code": code}
    return {"available": True, "outdated": data, "exit_code": code}


def external_skill_updates(repo: Path) -> Any:
    checker = repo / "tools" / "check_external_skill_updates.py"
    if not checker.exists():
        return {"available": False}
    code, out, err = run([sys.executable, str(checker), "--json"], timeout=90)
    if code != 0 and not out:
        return {"available": True, "error": err, "exit_code": code}
    try:
        return {"available": True, "results": json.loads(out), "exit_code": code}
    except json.JSONDecodeError:
        return {"available": True, "parse_error": out, "stderr": err, "exit_code": code}


def diff_snapshots(old: dict[str, Any] | None, new: dict[str, Any]) -> list[dict[str, Any]]:
    if not old:
        return [{"type": "baseline_created", "message": "No previous snapshot; current state saved as baseline."}]

    changes: list[dict[str, Any]] = []
    old_app = old.get("codex_app", {}).get("package_version")
    new_app = new.get("codex_app", {}).get("package_version")
    if old_app != new_app:
        changes.append({"type": "codex_app", "from": old_app, "to": new_app})

    old_groups = old.get("plugin_cache", {})
    new_groups = new.get("plugin_cache", {})
    for group, plugins in new_groups.items():
        for plugin, info in plugins.items():
            old_info = old_groups.get(group, {}).get(plugin, {})
            if old_info.get("latest") != info.get("latest") or old_info.get("versions") != info.get("versions"):
                changes.append(
                    {
                        "type": "plugin_cache",
                        "group": group,
                        "plugin": plugin,
                        "from": old_info.get("latest"),
                        "to": info.get("latest"),
                        "versions": info.get("versions"),
                    }
                )

    old_outdated = old.get("npm", {}).get("outdated", {})
    new_outdated = new.get("npm", {}).get("outdated", {})
    if old_outdated != new_outdated:
        changes.append({"type": "npm_outdated_changed", "from_count": len(old_outdated), "to_count": len(new_outdated)})

    old_ext = {
        item.get("skill"): (item.get("status"), item.get("local_ref"), item.get("latest_ref"))
        for item in old.get("external_skills", {}).get("results", [])
    }
    new_ext = {
        item.get("skill"): (item.get("status"), item.get("local_ref"), item.get("latest_ref"))
        for item in new.get("external_skills", {}).get("results", [])
    }
    for skill, state in sorted(new_ext.items()):
        if old_ext.get(skill) != state:
            changes.append({"type": "external_skill", "skill": skill, "from": old_ext.get(skill), "to": state})
    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description="Create and compare Codex capability/version snapshots.")
    parser.add_argument("--codex-home", type=Path, default=Path(os.environ.get("USERPROFILE", str(Path.home()))) / ".codex")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--snapshot-file", type=Path)
    parser.add_argument("--write", action="store_true", help="Write current snapshot after comparing.")
    args = parser.parse_args()

    snapshot_file = args.snapshot_file or args.codex_home / "version-snapshots" / "codex-capabilities-latest.json"
    old = None
    if snapshot_file.exists():
        old = json.loads(snapshot_file.read_text(encoding="utf-8"))

    current = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "codex_app": collect_codex_app(),
        "plugin_cache": collect_plugin_cache(args.codex_home),
        "npm": npm_outdated(),
        "external_skills": external_skill_updates(args.repo),
    }
    changes = diff_snapshots(old, current)
    result = {"snapshot_file": str(snapshot_file), "changes": changes, "current": current}
    print(json.dumps(result, ensure_ascii=False, indent=2))

    if args.write:
        snapshot_file.parent.mkdir(parents=True, exist_ok=True)
        snapshot_file.write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    sys.exit(main())
