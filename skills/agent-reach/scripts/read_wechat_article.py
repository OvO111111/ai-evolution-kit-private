from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup


def newest(paths: list[Path], since: float) -> Path | None:
    candidates = [path for path in paths if path.is_file() and path.stat().st_mtime >= since - 5]
    return max(candidates, key=lambda path: path.stat().st_mtime) if candidates else None


def recover_debug_html(debug_html: Path, output_root: Path) -> dict[str, object]:
    soup = BeautifulSoup(debug_html.read_text(encoding="utf-8", errors="replace"), "html.parser")
    title_node = soup.find("h1", id="activity-name")
    author_node = soup.find("span", id="js_name")
    content = soup.find("div", id="js_content")
    if content is None:
        raise RuntimeError("debug HTML does not contain div#js_content")

    block_names = {"p", "h1", "h2", "h3", "li", "blockquote", "pre"}
    blocks: list[str] = []
    for node in content.find_all(block_names):
        if any(parent.name in block_names for parent in node.parents if parent is not content):
            continue
        text = node.get_text(" ", strip=True)
        if text:
            blocks.append(text)
    body = "\n\n".join(blocks).strip()
    if len(body) < 200:
        raise RuntimeError(f"recovered body is too short: {len(body)} chars")

    title = title_node.get_text(" ", strip=True) if title_node else "wechat-article-recovered"
    author = author_node.get_text(" ", strip=True) if author_node else ""
    recovered = output_root / "recovered"
    recovered.mkdir(parents=True, exist_ok=True)
    output = recovered / f"wechat-{int(time.time())}.md"
    header = f"# {title}\n\n"
    if author:
        header += f"> Author: {author}\n\n"
    output.write_text(header + body + "\n", encoding="utf-8")
    return {"status": "ok", "mode": "debug_html_recovery", "title": title, "author": author, "chars": len(body), "output": str(output)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Read a public WeChat article with Camoufox and debug-HTML recovery.")
    parser.add_argument("url", nargs="?")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--tool-root", type=Path)
    parser.add_argument("--diagnose", action="store_true")
    args = parser.parse_args()

    home = Path.home()
    tool_root = args.tool_root or home / ".agent-reach" / "tools" / "wechat-article-for-ai"
    upstream_main = tool_root / "main.py"
    if not upstream_main.exists():
        print(json.dumps({"status": "not_ready", "missing": str(upstream_main)}, ensure_ascii=False))
        return 2
    if args.diagnose:
        print(json.dumps({"status": "ready", "python": sys.executable, "tool": str(upstream_main)}, ensure_ascii=False))
        return 0
    if not args.url or urlparse(args.url).hostname != "mp.weixin.qq.com":
        parser.error("url must use https://mp.weixin.qq.com/")

    output_root = args.output or Path(tempfile.gettempdir()) / "codex-wechat-reader"
    output_root.mkdir(parents=True, exist_ok=True)
    started = time.time()
    command = [sys.executable, str(upstream_main), args.url, "--no-images", "--force", "-o", str(output_root), "-v"]
    result = subprocess.run(command, cwd=tool_root, capture_output=True, text=True, encoding="utf-8", errors="replace")

    markdown = newest(list(output_root.rglob("*.md")), started)
    if result.returncode == 0 and markdown:
        content = markdown.read_text(encoding="utf-8", errors="replace")
        if len(content.strip()) >= 200:
            print(json.dumps({"status": "ok", "mode": "upstream_markdown", "title": markdown.stem, "chars": len(content), "output": str(markdown)}, ensure_ascii=False))
            return 0

    debug_roots = [tool_root / "output" / "debug", output_root / "debug"]
    debug_files = [path for root in debug_roots if root.exists() for path in root.rglob("*.html")]
    debug_html = newest(debug_files, started)
    if debug_html:
        try:
            print(json.dumps(recover_debug_html(debug_html, output_root), ensure_ascii=False))
            return 0
        except Exception as exc:
            recovery_error = str(exc)
    else:
        recovery_error = "no fresh debug HTML was produced"

    combined = "\n".join([result.stdout, result.stderr]).strip()
    print(json.dumps({"status": "failed", "returncode": result.returncode, "recovery_error": recovery_error, "diagnostic": combined[-2000:]}, ensure_ascii=False))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
