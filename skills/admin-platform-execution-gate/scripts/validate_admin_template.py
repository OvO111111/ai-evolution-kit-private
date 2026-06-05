from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "assets" / "admin-console-reference.html"

REQUIRED = {
    "app shell": [r"grid-template-columns:\s*248px", r"grid-template-rows:\s*58px"],
    "decision metrics": [r"class=\"decision\"", r"最近全量通过率", r"受影响产品", r"告警送达"],
    "table workflow": [r"<table>", r"产品检测结果", r"失败原因|关键原因", r"sticky"],
    "detail pattern": [r"class=\"drawer\"", r"失败详情", r"创建修复单"],
    "state vocabulary": [r"通过", r"失败", r"待复核", r"empty/error/loading|disabled|status"],
}


def main() -> int:
    if not TEMPLATE.exists():
        print(f"missing template: {TEMPLATE}")
        return 1
    html = TEMPLATE.read_text(encoding="utf-8")
    failed: list[str] = []
    for group, patterns in REQUIRED.items():
        for pattern in patterns:
            if not re.search(pattern, html, re.I):
                failed.append(f"{group}: missing {pattern}")
    if len(html) < 9000:
        failed.append("template too small to be a real admin reference")
    if re.search(r"hero|marketing|gradient-orb|bokeh", html, re.I):
        failed.append("template contains marketing/hero decoration language")
    if html.count('class="metric"') > 5:
        failed.append("too many metric cards for first-screen admin decision")
    if failed:
        print("admin_template=FAIL")
        for item in failed:
            print(f"- {item}")
        return 1
    print("admin_template=PASS")
    print(f"template={TEMPLATE}")
    print(f"bytes={TEMPLATE.stat().st_size}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
