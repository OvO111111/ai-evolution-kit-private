from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CASES = [
    {
        "id": "generic_h5",
        "request": "做一个与公司项目无关的个人旅行计划 H5。产品目标、用户和页面方向已经清楚；这是普通个人项目，不复用统一后台或公司 H5。",
        "expected_groups": [["product-design:index", "Product Design", "index"]],
        "forbidden": ["app-factory-h5-admin", "huashu-design"],
        "sequence": [],
    },
    {
        "id": "company_h5",
        "request": "在公司的统一后台体系上做第二个项目“每周穿搭”。先完成分析和 H5，H5 确认后再做后台，后台确认后再写 PRD。",
        "expected_groups": [["app-factory-h5-admin"]],
        "forbidden": [],
        "sequence": ["H5", ["admin", "后台"], "PRD"],
        "must_read": ["app-factory-h5-admin"],
    },
    {
        "id": "admin_redesign",
        "request": "这个内部工具平台后台结构混乱、卡片堆砌、按钮还是假的。直接给出完整重做路径，不要一步一问，也不要套公司 H5。",
        "expected_groups": [["ui-product-design-router"], ["admin-platform-execution-gate"]],
        "forbidden": ["app-factory-h5-admin"],
        "sequence": [],
    },
    {
        "id": "prd_source_gate",
        "request": "根据项目里已经存在的 PRD、HTML 原型和客户样本重写一份可评审 PRD。必须先读真实资料，不能先套模板。",
        "expected_groups": [["pm-prd"]],
        "forbidden": [],
        "sequence": ["读取", "PRD"],
    },
    {
        "id": "four_design_lanes",
        "request": "给同一个后台首页做 4 个完全不同的设计方案，分别用 huashu、Product Design、open-design 和 taste-skill，不能只是换颜色。",
        "expected_groups": [
            ["ui-product-design-router"],
            ["admin-platform-execution-gate"],
            ["huashu-design"],
            ["Product Design", "product-design:index", "index"],
            ["open-design-design-systems"],
            ["design-taste-frontend"],
        ],
        "forbidden": [],
        "sequence": [],
    },
    {
        "id": "chrome_login_doc",
        "request": "读取我当前 Chrome 里已经登录打开的微信文档，必须使用现有登录态，不要用 guest 抓取代替。只做读取。",
        "expected_groups": [["chrome:control-chrome", "control-chrome", "Chrome"]],
        "forbidden": [],
        "sequence": [],
    },
    {
        "id": "windows_excel",
        "request": "打开我电脑上的 Excel 桌面软件，检查当前工作簿的可见表头和活动工作表，不修改内容。",
        "expected_groups": [["computer-use:computer-use", "computer-use", "Computer Use"]],
        "forbidden": ["desktop-control"],
        "sequence": [],
    },
    {
        "id": "feishu_project_sync",
        "request": "把当前项目已经确认的 PRD 和 HTML 原型上传并同步到飞书项目归档，保持可编辑和版本对应。",
        "expected_groups": [["feishu-prd-html-sync"]],
        "forbidden": ["hermes"],
        "sequence": [],
    },
    {
        "id": "public_wechat_article",
        "request": "学习这个公开微信公众号文章链接。先用最低成本方式读取；如果静态抓取失败，再升级到浏览器或站点专用工具。",
        "expected_groups": [["web-access"]],
        "forbidden": ["computer-use:computer-use", "desktop-control"],
        "sequence": [],
    },
    {
        "id": "analysis_report",
        "request": "根据一个 Excel 文件生成专业的数据分析报告：先校验数据质量，再做指标、趋势、异常和建议，最终需要可复核的报告。",
        "expected_groups": [["data-analysis-report"], ["spreadsheets:Spreadsheets", "Spreadsheets"]],
        "forbidden": [],
        "sequence": [],
    },
    {
        "id": "official_pdf",
        "request": "读取一个 PDF，提取表格并核对页面布局。官方 PDF 插件当前可用，必须优先用官方能力。",
        "expected_groups": [["pdf:pdf", "official PDF", "primary-runtime PDF"]],
        "forbidden": ["pdf-legacy-fallback"],
        "sequence": [],
    },
    {
        "id": "official_word",
        "request": "创建并编辑一份 Word DOCX，包含标题层级、表格、批注和修订，最后做视觉检查。官方 Documents 插件可用。",
        "expected_groups": [["documents:documents", "official Documents"]],
        "forbidden": ["docx-legacy-fallback"],
        "sequence": [],
    },
    {
        "id": "official_presentation",
        "request": "根据现有资料制作一份 PowerPoint，沿用模板、编辑图表并检查每页排版。官方 Presentations 插件可用。",
        "expected_groups": [["presentations:Presentations", "official Presentations"]],
        "forbidden": ["pptx-legacy-fallback"],
        "sequence": [],
    },
    {
        "id": "in_app_browser",
        "request": "在临时浏览器里打开一个公开动态网页，点击筛选器并读取结果。不需要我的 Chrome 登录态，也不是本地开发页面。",
        "expected_groups": [["browser:control-in-app-browser", "control-in-app-browser"]],
        "forbidden": ["chrome:control-chrome", "browser-cdp-fallback"],
        "sequence": [],
    },
    {
        "id": "feishu_whiteboard",
        "request": "在飞书画板中画一个可编辑的审批流程图，需要后续继续修改节点和连线。",
        "expected_groups": [["diagram-drawing-router"], ["lark-whiteboard"]],
        "forbidden": ["desktop-control-fallback", "hermes"],
        "sequence": [],
    },
    {
        "id": "feishu_drive_upload",
        "request": "把一个本地 PDF 上传到指定飞书云盘文件夹。这不是项目 PRD/HTML 归档，也不需要改文档正文。",
        "expected_groups": [["lark-drive"]],
        "forbidden": ["feishu-prd-html-sync", "hermes"],
        "sequence": [],
    },
    {
        "id": "lark_group_read",
        "request": "搜索并读取一个飞书工作群最近的消息，整理上下文但不要发送回复。",
        "expected_groups": [["lark-im"]],
        "forbidden": ["wechat-work-context"],
        "sequence": [],
    },
    {
        "id": "wechat_pay_product",
        "request": "梳理微信支付 H5 支付与委托扣款的产品路径、申请条件、材料、风险和验收边界，不要写支付 SDK 代码。",
        "expected_groups": [["wechat-pay-product-design"]],
        "forbidden": ["app-factory-h5-admin"],
        "sequence": [],
    },
    {
        "id": "wechat_work_context",
        "request": "读取允许范围内的两个微信工作群历史，保持群隔离，帮我理解上下文并起草回复，但不要发送。",
        "expected_groups": [["wechat-work-context"]],
        "forbidden": ["lark-im", "computer-use:computer-use"],
        "sequence": [],
    },
    {
        "id": "scan_ocr",
        "request": "从一批扫描图片中提取中文正文和表格，先做轻量 OCR，失败页再升级，不涉及 PDF 编辑。",
        "expected_groups": [["ocr-and-documents"]],
        "forbidden": ["pdf-legacy-fallback", "documents:documents"],
        "sequence": [],
    },
    {
        "id": "diagram_router",
        "request": "把系统模块和数据流画成可编辑的本地 HTML 架构图。先判断最合适的绘图技术，不要上传飞书。",
        "expected_groups": [["diagram-drawing-router"]],
        "forbidden": ["lark-whiteboard"],
        "sequence": [],
    },
    {
        "id": "evolution_intake",
        "request": "评估这个外部 Agent 项目 URL `https://github.com/example/agent-project` 是否值得吸收到全局能力。先读来源、查重叠、写采纳或拒绝策略并做小测试，不要直接全盘安装。",
        "expected_groups": [["absorb-lessons"], ["web-access"]],
        "forbidden": ["skill-installer"],
        "sequence": [],
    },
    {
        "id": "black_box_user_walkthrough",
        "request": "公司刚做完一个 H5。请把自己当成第一次使用它的普通用户，不看代码，真实点击主要流程，检查哪里会迷路、报错、状态不清或返回后丢数据；发现问题后再修复并重走同一流程。",
        "expected_groups": [["adversarial-review"]],
        "forbidden": ["project-prd-audit", "project-prd-h5-audit"],
        "sequence": [["黑盒", "盲测"], "修复", ["回归", "重走", "复测"]],
        "allow_waiting": True,
        "must_read": ["adversarial-review"],
    },
    {
        "id": "red_team_evolution_plan",
        "request": "先不要执行。我要把所有产品、设计和进化任务都强制走一套重型多 Agent 流程，并把细节写进全局 AGENTS.md。请先做红队审查和最小证伪实验，再给一个明确结论。",
        "expected_groups": [["adversarial-review"], ["absorb-lessons"]],
        "forbidden": ["cavecrew"],
        "sequence": ["红队", ["证伪", "盲测", "阈值"], "结论"],
        "must_read": ["adversarial-review", "absorb-lessons"],
    },
    {
        "id": "first_principles_adversarial_decision",
        "request": "从第一性原理出发，评估是否把所有内部工具从现有 PostgreSQL 迁移到事件溯源。开启对抗式审查。先不要执行；给出明确结论和最小证伪实验。",
        "expected_groups": [["adversarial-review"]],
        "forbidden": [],
        "sequence": [
            ["目标", "goal"],
            ["证据", "evidence"],
            ["失败", "failure"],
            ["实验", "experiment"],
        ],
        "must_include": [["结论", "decision", "experiment first"]],
        "must_read": ["adversarial-review"],
    },
    {
        "id": "low_risk_no_red_team",
        "request": "把已确认页面的按钮文案从‘下一步’改成‘继续’，这是可随时撤销的小改动。直接修改并做一次页面验证，不要扩大范围。",
        "expected_groups": [],
        "forbidden": ["adversarial-review"],
        "sequence": [],
    },
    {
        "id": "company_h5_black_box_checkpoint",
        "request": "每周穿搭 H5 已经做完，现在到 H5 确认前的验收节点。不要先看代码，请按公司 H5 流程执行第一次用户黑盒走查，冻结问题后再修复并复测。",
        "expected_groups": [["app-factory-h5-admin"], ["adversarial-review"]],
        "forbidden": ["project-prd-audit", "project-prd-h5-audit"],
        "sequence": [["黑盒", "盲测"], ["冻结", "问题"], "修复", ["复测", "重走", "回归"]],
        "must_read": ["app-factory-h5-admin", "adversarial-review"],
    },
    {
        "id": "metabase_bi",
        "request": "检查现有自托管 Metabase 项目的指标口径、字段中文名、筛选器和新旧报表一致性，必须基于项目真实脚本和表。",
        "expected_groups": [["metabase-bi-semantic-layer"]],
        "forbidden": ["app-factory-h5-admin"],
        "sequence": [],
    },
    {
        "id": "data_dashboard",
        "request": "基于结构化业务数据设计一个可复核的经营仪表盘，先检查数据质量、定义 KPI，再构建可视化。",
        "expected_groups": [["data-analytics:build-dashboard", "build-dashboard", "data-analysis-report"]],
        "preferred_groups": [["data-analytics:build-dashboard", "build-dashboard"]],
        "forbidden": ["open-design-design-systems"],
        "sequence": [],
    },
    {
        "id": "video_frames",
        "request": "从本地视频的 10 秒、30 秒和 60 秒处各提取一帧，供我检查画面，不做视频剪辑。",
        "expected_groups": [["video-frames"]],
        "forbidden": ["computer-use:computer-use"],
        "sequence": [],
        "allow_waiting": True,
    },
    {
        "id": "github_triage",
        "request": "检查 GitHub 仓库当前 PR、issue 和 CI 状态，给出处理顺序，但先不要合并、关闭或发布。",
        "expected_groups": [["github:github", "GitHub"]],
        "forbidden": ["github:yeet"],
        "sequence": [],
    },
]


def latest_codex() -> Path:
    root = Path(os.environ.get("LOCALAPPDATA", "")) / "OpenAI" / "Codex" / "bin"
    candidates = sorted(root.glob("*/codex.exe"), key=lambda path: path.stat().st_mtime, reverse=True)
    if not candidates:
        raise FileNotFoundError(f"codex.exe not found under {root}")
    return candidates[0]


def clean_json_text(text: str) -> dict[str, Any]:
    candidate = text.strip()
    if candidate.startswith("```"):
        candidate = re.sub(r"^```(?:json)?\s*", "", candidate)
        candidate = re.sub(r"\s*```$", "", candidate)
    return json.loads(candidate)


def normalize_selected(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value]
    return []


def run_case(codex: Path, model: str, cwd: Path, case: dict[str, Any], timeout: int) -> dict[str, Any]:
    prompt = f"""下面是一个真实用户请求。执行正常的 skill gate，并完整读取你选择的 SKILL.md；这是只读路由回归测试，不修改文件、不操作外部账号、不实际打开应用。

用户请求：{case['request']}

最终只返回 JSON 对象：
{{
  "selected_skills": ["使用当前目录中的准确 skill 标识"],
  "excluded_skills": ["明确排除且容易误触发的 skill"],
  "ordered_actions": ["不超过 6 个实际执行步骤"],
  "blocking_questions": ["一次列出全部真正阻塞的问题，最多 3 个"],
  "would_continue_without_waiting": true,
  "scope_reason": "一句话说明项目/能力边界"
}}
不要在 JSON 外输出解释。"""
    command = [
        str(codex), "exec", "--ephemeral", "--sandbox", "read-only", "--skip-git-repo-check",
        "-m", model, "--json", "-C", str(cwd), prompt,
    ]
    env = dict(os.environ)
    env["PYTHONUTF8"] = "1"
    proc = subprocess.run(
        command,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        env=env,
    )
    messages: list[str] = []
    read_folders: set[str] = set()
    usage: dict[str, Any] | None = None
    parse_errors = 0
    for line in proc.stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            parse_errors += 1
            continue
        if event.get("type") == "item.completed":
            item = event.get("item") or {}
            if item.get("type") == "agent_message" and isinstance(item.get("text"), str):
                messages.append(item["text"])
            if item.get("type") == "command_execution":
                command_text = str(item.get("command") or "")
                for folder in re.findall(r"([A-Za-z0-9][A-Za-z0-9._:-]{0,100})[\\/]+SKILL\.md", command_text, re.I):
                    read_folders.add(folder)
        if event.get("type") == "turn.completed":
            usage = event.get("usage")

    final_obj: dict[str, Any] = {}
    final_error: str | None = None
    if messages:
        try:
            final_obj = clean_json_text(messages[-1])
        except (json.JSONDecodeError, TypeError) as exc:
            final_error = str(exc)
    else:
        final_error = "no agent message"

    selected = normalize_selected(final_obj.get("selected_skills"))
    selected_folded = "\n".join(selected).casefold()
    failures: list[str] = []
    preference_misses: list[str] = []
    for expected_group in case["expected_groups"]:
        if not any(alias.casefold() in selected_folded for alias in expected_group):
            failures.append(f"missing expected route: {expected_group}")
    for preferred_group in case.get("preferred_groups") or []:
        if not any(alias.casefold() in selected_folded for alias in preferred_group):
            preference_misses.append(f"preferred route unavailable or not selected: {preferred_group}")
    for forbidden in case["forbidden"]:
        if forbidden.casefold() in selected_folded:
            failures.append(f"forbidden route selected: {forbidden}")
    actions_text = "\n".join(str(item) for item in final_obj.get("ordered_actions") or [])
    last_pos = -1
    for token in case["sequence"]:
        aliases = token if isinstance(token, list) else [token]
        positions = [
            actions_text.casefold().find(str(alias).casefold(), last_pos + 1)
            for alias in aliases
        ]
        matching_positions = [pos for pos in positions if pos >= 0]
        if not matching_positions:
            failures.append(f"missing/out-of-order action token: {aliases}")
            break
        last_pos = min(matching_positions)
    for token in case.get("must_include") or []:
        aliases = token if isinstance(token, list) else [token]
        if not any(str(alias).casefold() in actions_text.casefold() for alias in aliases):
            failures.append(f"missing required action token: {aliases}")
    read_folders_folded = {folder.casefold() for folder in read_folders}
    for folder in case.get("must_read") or []:
        if folder.casefold() not in read_folders_folded:
            failures.append(f"selected workflow was not opened: {folder}")
    questions = final_obj.get("blocking_questions") or []
    if not isinstance(questions, list) or len(questions) > 3:
        failures.append("blocking_questions is not a list of at most 3 items")
    if not case.get("allow_waiting") and final_obj.get("would_continue_without_waiting") is not True:
        failures.append("would_continue_without_waiting is not true")
    if final_error:
        failures.append(f"final JSON parse failed: {final_error}")
    if proc.returncode != 0:
        failures.append(f"codex exec exit code {proc.returncode}")

    stderr_signals = [
        line for line in proc.stderr.splitlines()
        if " WARN " in line or " ERROR " in line or "failed" in line.casefold()
    ]
    return {
        "case_id": case["id"],
        "passed": not failures,
        "degraded": not failures and bool(preference_misses),
        "failures": failures,
        "preference_misses": preference_misses,
        "selected_skills": selected,
        "excluded_skills": final_obj.get("excluded_skills") or [],
        "ordered_actions": final_obj.get("ordered_actions") or [],
        "blocking_questions": questions if isinstance(questions, list) else [],
        "would_continue_without_waiting": final_obj.get("would_continue_without_waiting"),
        "scope_reason": final_obj.get("scope_reason"),
        "skill_folders_read": sorted(read_folders),
        "returncode": proc.returncode,
        "usage": usage,
        "stdout_parse_errors": parse_errors,
        "stderr_signals": stderr_signals[:20],
    }


def build_report(results: list[dict[str, Any]], model: str, codex: Path) -> dict[str, Any]:
    ordered = sorted(results, key=lambda row: row["case_id"])
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "codex": f"codex.exe@{codex.parent.name}",
        "cases": len(ordered),
        "passed": sum(1 for row in ordered if row.get("passed")),
        "failed": sum(1 for row in ordered if not row.get("passed")),
        "degraded": sum(1 for row in ordered if row.get("degraded")),
        "results": ordered,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="gpt-5.6-sol")
    parser.add_argument(
        "--workers",
        type=int,
        default=1,
        help="Requested worker count. Kept at 1 unless --allow-parallel is explicit.",
    )
    parser.add_argument(
        "--allow-parallel",
        action="store_true",
        help="Allow concurrent codex exec processes; may race on shared model/plugin caches.",
    )
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--case", action="append", dest="case_ids")
    args = parser.parse_args()

    codex = latest_codex()
    eval_cwd = Path.home() / ".codex" / "tmp" / "evolution-route-evals"
    eval_cwd.mkdir(parents=True, exist_ok=True)
    selected_cases = [case for case in CASES if not args.case_ids or case["id"] in args.case_ids]
    results: list[dict[str, Any]] = []
    worker_count = max(1, args.workers) if args.allow_parallel else 1
    with ThreadPoolExecutor(max_workers=worker_count) as pool:
        futures = {
            pool.submit(run_case, codex, args.model, eval_cwd, case, args.timeout): case["id"]
            for case in selected_cases
        }
        for future in as_completed(futures):
            case_id = futures[future]
            try:
                results.append(future.result())
            except Exception as exc:  # noqa: BLE001 - evaluation harness records per-case failures.
                results.append({"case_id": case_id, "passed": False, "failures": [repr(exc)]})

            partial_report = build_report(results, args.model, codex)
            if args.out:
                args.out.parent.mkdir(parents=True, exist_ok=True)
                args.out.write_text(json.dumps(partial_report, ensure_ascii=False, indent=2), encoding="utf-8")
            latest = next(row for row in partial_report["results"] if row["case_id"] == case_id)
            print(
                json.dumps(
                    {
                        "case_completed": case_id,
                        "passed": latest.get("passed", False),
                        "failures": latest.get("failures", []),
                    },
                    ensure_ascii=False,
                ),
                flush=True,
            )

    report = build_report(results, args.model, codex)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
