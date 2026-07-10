from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {
    ".md",
    ".json",
    ".jsonl",
    ".yaml",
    ".yml",
    ".toml",
    ".py",
    ".ps1",
    ".js",
    ".mjs",
    ".ts",
    ".tsx",
    ".jsx",
    ".txt",
    ".html",
    ".css",
}
RULES = {
    "personal_windows_path": re.compile(
        r"C:(?:\\{1,2}|/)Users(?:\\{1,2}|/)skzjc", re.IGNORECASE
    ),
    "private_company_root": re.compile(
        r"D:(?:\\{1,2}|/)xiaochengxu", re.IGNORECASE
    ),
    "feishu_document_url": re.compile(
        r"https://(?:my\.)?feishu\.cn/(?:docx|wiki|base|sheets)/[A-Za-z0-9_-]{8,}",
        re.IGNORECASE,
    ),
    "lark_identity_or_app_id": re.compile(r"\b(?:ou_|cli_)[A-Za-z0-9]{12,}\b"),
    "labeled_document_token": re.compile(
        r"(?i)(?:whiteboard|board|document|doc)\s*(?:id|token)\s*[:=]\s*[A-Za-z0-9_-]{12,}"
    ),
    "known_private_host": re.compile(r"\b(?:47\.107\.61\.166|8\.129\.82\.112)\b"),
    "known_private_email": re.compile(
        r"\b(?:support@tengwei\.cn|zhousy@96225\.com)\b", re.IGNORECASE
    ),
    "known_private_phone": re.compile(r"\b4006021400\b"),
    "openai_style_secret": re.compile(r"\bsk-[A-Za-z0-9_-]{12,}\b"),
}


def candidate_files() -> list[Path]:
    proc = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=False,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if proc.returncode == 0:
        return [ROOT / line for line in proc.stdout.splitlines() if line.strip()]
    return [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]


def main() -> int:
    findings: list[dict[str, object]] = []
    scanned = 0
    for path in candidate_files():
        if path.suffix.casefold() not in TEXT_SUFFIXES or not path.exists():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if "\x00" in text:
            continue
        scanned += 1
        for line_number, line in enumerate(text.splitlines(), 1):
            for rule, pattern in RULES.items():
                if pattern.search(line):
                    findings.append(
                        {
                            "rule": rule,
                            "path": path.relative_to(ROOT).as_posix(),
                            "line": line_number,
                        }
                    )

    report = {
        "files_scanned": scanned,
        "findings": len(findings),
        "rules": sorted(RULES),
        "items": findings,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
