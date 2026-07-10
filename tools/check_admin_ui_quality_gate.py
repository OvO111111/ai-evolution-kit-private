from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


FILES = [
    ROOT / "AGENTS.md",
    ROOT / "skills" / "admin-platform-execution-gate" / "SKILL.md",
    ROOT / "skills" / "open-design-design-systems" / "SKILL.md",
    ROOT / "memories" / "vault_summaries" / "skill-routing.md",
]

REQUIRED_PHRASES = {
    "natural_complaints": ["丑", "垃圾", "像新人", "skill 没用上"],
    "loop_breaker": ["Redesign Loop Breaker", "stop incremental patching"],
    "template_first": ["Template-First Rule", "admin-console-reference.html"],
    "concrete_contract": [
        "app shell",
        "navigation model",
        "first-screen decision",
        "table density",
        "detail drawer",
        "action states",
        "empty/error/loading",
    ],
    "anti_fake_adoption": ["not adoption", "only the colors changed"],
}


def main() -> int:
    missing: list[str] = []
    combined = ""
    for path in FILES:
        if not path.exists():
            missing.append(f"missing file: {path}")
            continue
        combined += "\n" + path.read_text(encoding="utf-8", errors="ignore")

    lower = combined.lower()
    for group, phrases in REQUIRED_PHRASES.items():
        for phrase in phrases:
            if phrase.lower() not in lower:
                missing.append(f"{group}: missing phrase {phrase!r}")

    if missing:
        print("admin_ui_quality_gate=FAIL")
        for item in missing:
            print(f"- {item}")
        return 1

    print("admin_ui_quality_gate=PASS")
    print(f"checked_files={len(FILES)}")
    print(f"required_groups={len(REQUIRED_PHRASES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
