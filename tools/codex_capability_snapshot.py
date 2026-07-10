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


def resolve_codex_cli(codex_home: Path) -> str | None:
    env_path = os.environ.get("CODEX_CLI_PATH")
    if env_path and Path(env_path).exists():
        return env_path

    config_file = codex_home / "config.toml"
    if config_file.exists():
        config_text = config_file.read_text(encoding="utf-8", errors="ignore")
        match = re.search(r"CODEX_CLI_PATH\s*=\s*['\"]([^'\"]+)['\"]", config_text)
        if match and Path(match.group(1)).exists():
            return match.group(1)

    local_appdata = os.environ.get("LOCALAPPDATA")
    if local_appdata:
        bin_root = Path(local_appdata) / "OpenAI" / "Codex" / "bin"
        candidates = sorted(
            bin_root.glob("*/codex.exe"),
            key=lambda path: path.stat().st_mtime if path.exists() else 0,
            reverse=True,
        )
        if candidates:
            return str(candidates[0])

    return shutil.which("codex")


def collect_installed_plugins(codex_home: Path) -> dict[str, Any]:
    codex_cli = resolve_codex_cli(codex_home)
    if not codex_cli:
        return {"available": False, "message": "No usable codex CLI found."}

    code, out, err = run([codex_cli, "plugin", "list", "--json"], timeout=60)
    if code != 0 and not out:
        return {"available": True, "cli": codex_cli, "error": err, "exit_code": code}
    try:
        payload = json.loads(out)
    except json.JSONDecodeError:
        return {"available": True, "cli": codex_cli, "parse_error": out, "stderr": err, "exit_code": code}

    installed = payload.get("installed", []) if isinstance(payload, dict) else []
    compact = []
    for item in installed:
        compact.append(
            {
                "pluginId": item.get("pluginId"),
                "name": item.get("name"),
                "marketplaceName": item.get("marketplaceName"),
                "version": item.get("version"),
                "installed": item.get("installed"),
                "enabled": item.get("enabled"),
                "authPolicy": item.get("authPolicy"),
                "source": item.get("source"),
            }
        )
    return {"available": True, "cli": codex_cli, "installed": compact, "exit_code": code}


def collect_lark_cli() -> dict[str, Any]:
    source = powershell("(Get-Command lark-cli -ErrorAction SilentlyContinue).Source")
    if not source:
        return {"available": False, "message": "No lark-cli found on PATH."}

    probe_env = "$env:HERMES_HOME='C:\\hermes-probe'; $env:LARKSUITE_CLI_NO_UPDATE_NOTIFIER='1'; $env:LARKSUITE_CLI_NO_SKILLS_NOTIFIER='1'; "
    version_out = powershell(probe_env + "lark-cli --version", timeout=20)
    update_out = powershell(probe_env + "lark-cli update --check --json", timeout=60)
    parsed_update = None
    if update_out:
        try:
            parsed_update = json.loads(update_out)
        except json.JSONDecodeError:
            parsed_update = {"parse_error": update_out}

    return {
        "available": True,
        "source": source,
        "version_output": version_out,
        "update_check": parsed_update,
    }


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

    old_plugins = {
        item.get("pluginId"): (item.get("version"), item.get("installed"), item.get("enabled"))
        for item in old.get("installed_plugins", {}).get("installed", [])
    }
    new_plugins = {
        item.get("pluginId"): (item.get("version"), item.get("installed"), item.get("enabled"))
        for item in new.get("installed_plugins", {}).get("installed", [])
    }
    for plugin_id, state in sorted(new_plugins.items()):
        if old_plugins.get(plugin_id) != state:
            changes.append({"type": "installed_plugin", "plugin": plugin_id, "from": old_plugins.get(plugin_id), "to": state})
    for plugin_id, state in sorted(old_plugins.items()):
        if plugin_id not in new_plugins:
            changes.append({"type": "installed_plugin_removed", "plugin": plugin_id, "from": state, "to": None})

    def lark_state(snapshot: dict[str, Any]) -> tuple[Any, ...]:
        check = snapshot.get("lark_cli", {}).get("update_check", {}) or {}
        skills = check.get("skills_status", {}) or {}
        return (
            check.get("current_version"),
            check.get("latest_version"),
            skills.get("current"),
            skills.get("target"),
            skills.get("in_sync"),
            skills.get("official"),
            skills.get("updated"),
        )

    old_lark = lark_state(old)
    new_lark = lark_state(new)
    if old_lark != new_lark:
        changes.append({"type": "lark_cli", "from": old_lark, "to": new_lark})

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
        "installed_plugins": collect_installed_plugins(args.codex_home),
        "lark_cli": collect_lark_cli(),
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
