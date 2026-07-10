from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*", re.DOTALL)
GITHUB_RE = re.compile(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")
SEMVER_RE = re.compile(r"^v?(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:[-+].*)?$")


@dataclass
class SkillUpdateStatus:
    skill: str
    path: str
    status: str
    upstream: str | None = None
    local_ref: str | None = None
    local_commit: str | None = None
    latest_ref: str | None = None
    latest_commit: str | None = None
    github_urls: list[str] | None = None
    message: str | None = None


def parse_frontmatter(text: str) -> dict[str, Any]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def semver_key(tag: str) -> tuple[int, int, int, str]:
    clean = tag.rsplit("/", 1)[-1]
    match = SEMVER_RE.match(clean)
    if not match:
        return (-1, -1, -1, clean)
    major = int(match.group(1) or 0)
    minor = int(match.group(2) or 0)
    patch = int(match.group(3) or 0)
    return (major, minor, patch, clean)


def run_git_ls_remote(url: str, pattern: str) -> list[tuple[str, str]]:
    proc = subprocess.run(
        ["git", "ls-remote", "--tags", "--refs", url, pattern],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git ls-remote failed: {url}")
    rows: list[tuple[str, str]] = []
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) == 2:
            rows.append((parts[0], parts[1]))
    return rows


def latest_tag(url: str) -> tuple[str | None, str | None]:
    rows = run_git_ls_remote(url, "*")
    tags = [(commit, ref.rsplit("/", 1)[-1]) for commit, ref in rows if SEMVER_RE.match(ref.rsplit("/", 1)[-1])]
    if not tags:
        return None, None
    commit, tag = sorted(tags, key=lambda item: semver_key(item[1]))[-1]
    return tag, commit


def check_skill(skill_file: Path) -> SkillUpdateStatus | None:
    text = skill_file.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    skill = meta.get("name") or skill_file.parent.name
    upstream_meta = meta.get("metadata") if isinstance(meta.get("metadata"), dict) else {}
    upstream = upstream_meta.get("upstream") or meta.get("upstream") or None
    local_ref = upstream_meta.get("upstream_ref") or meta.get("upstream_ref") or None
    local_commit = upstream_meta.get("upstream_commit") or meta.get("upstream_commit") or None
    github_urls = sorted(set(GITHUB_RE.findall(text)))

    if not upstream:
        if github_urls:
            return SkillUpdateStatus(
                skill=skill,
                path=str(skill_file),
                status="needs_metadata",
                github_urls=github_urls,
                message="GitHub URLs found, but no upstream metadata; cannot honestly check updates.",
            )
        return None

    if "github.com/" not in upstream:
        return SkillUpdateStatus(
            skill=skill,
            path=str(skill_file),
            status="unsupported_upstream",
            upstream=upstream,
            local_ref=local_ref,
            local_commit=local_commit,
            message="Only GitHub upstreams are implemented by this checker.",
        )

    try:
        ref, commit = latest_tag(upstream)
    except Exception as exc:  # noqa: BLE001
        return SkillUpdateStatus(
            skill=skill,
            path=str(skill_file),
            status="check_failed",
            upstream=upstream,
            local_ref=local_ref,
            local_commit=local_commit,
            message=str(exc),
        )

    if not ref:
        return SkillUpdateStatus(
            skill=skill,
            path=str(skill_file),
            status="no_semver_tags",
            upstream=upstream,
            local_ref=local_ref,
            local_commit=local_commit,
            message="No semver-like tags found upstream.",
        )

    if local_ref == ref and (not local_commit or local_commit == commit):
        status = "current"
        message = "Local upstream metadata matches latest tag."
    elif local_ref == ref and local_commit and local_commit != commit:
        status = "tag_commit_changed"
        message = "Same tag name but different commit; inspect before trusting."
    else:
        status = "update_available"
        message = "Newer upstream tag exists or local metadata is incomplete."

    return SkillUpdateStatus(
        skill=skill,
        path=str(skill_file),
        status=status,
        upstream=upstream,
        local_ref=local_ref,
        local_commit=local_commit,
        latest_ref=ref,
        latest_commit=commit,
        github_urls=github_urls,
        message=message,
    )


def default_roots() -> list[Path]:
    home = Path(os.environ.get("USERPROFILE") or Path.home())
    return [home / ".codex" / "skills", home / ".agents" / "skills"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Check external/upstream skill update status.")
    parser.add_argument("--root", action="append", type=Path, help="Skill root to scan. Can be repeated.")
    parser.add_argument("--json", action="store_true", help="Emit JSON only.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero for updates, metadata gaps, or failures.")
    args = parser.parse_args()

    roots = args.root or default_roots()
    results: list[SkillUpdateStatus] = []
    for root in roots:
        if not root.exists():
            continue
        for skill_file in sorted(root.glob("*/SKILL.md")):
            result = check_skill(skill_file)
            if result:
                results.append(result)

    if args.json:
        print(json.dumps([asdict(item) for item in results], ensure_ascii=False, indent=2))
    else:
        print(f"checked_roots={len([root for root in roots if root.exists()])}")
        print(f"external_or_github_skills={len(results)}")
        counts: dict[str, int] = {}
        for item in results:
            counts[item.status] = counts.get(item.status, 0) + 1
        for status, count in sorted(counts.items()):
            print(f"{status}={count}")
        print()
        for item in results:
            latest = f" latest={item.latest_ref or '-'}"
            local = f" local={item.local_ref or '-'}"
            print(f"[{item.status}] {item.skill}{local}{latest} :: {item.message}")
            if item.status == "needs_metadata" and item.github_urls:
                print(f"  urls={'; '.join(item.github_urls[:5])}")

    bad_statuses = {"update_available", "tag_commit_changed", "check_failed", "needs_metadata", "unsupported_upstream"}
    if args.strict and any(item.status in bad_statuses for item in results):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
