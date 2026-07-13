from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path


CODEX_HOME = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
AGENTS_HOME = Path.home() / ".agents"
EXPORT_ROOT = Path(__file__).resolve().parents[1]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(path: Path) -> dict[str, str]:
    text = read(path)
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    values: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip("'\"")
    return values


def latest_version_dir(plugin: Path) -> Path:
    versions = [path for path in plugin.iterdir() if path.is_dir() and path.name.casefold() != "latest"]
    if not versions:
        raise FileNotFoundError(f"no version directory under {plugin}")
    return max(versions, key=lambda path: path.stat().st_mtime)


def main() -> int:
    failures: list[str] = []
    checks: list[str] = []

    paths = {
        "router": CODEX_HOME / "skills" / "ui-product-design-router" / "SKILL.md",
        "app_factory": CODEX_HOME / "skills" / "app-factory-h5-admin" / "SKILL.md",
        "admin_gate": CODEX_HOME / "skills" / "admin-platform-execution-gate" / "SKILL.md",
        "pm_prd": CODEX_HOME / "skills" / "pm-prd" / "SKILL.md",
        "agent_reach": CODEX_HOME / "skills" / "agent-reach" / "SKILL.md",
        "agent_reach_reference": AGENTS_HOME / "skills" / "agent-reach" / "SKILL.md",
        "image_fallback": CODEX_HOME / "skills" / "image-to-code" / "SKILL.md",
        "pdf_fallback": CODEX_HOME / "skills" / "pdf" / "SKILL.md",
        "xlsx_fallback": CODEX_HOME / "skills" / "xlsx" / "SKILL.md",
        "docx_fallback": CODEX_HOME / "skills" / "docx" / "SKILL.md",
        "pptx_fallback": CODEX_HOME / "skills" / "pptx" / "SKILL.md",
        "browser_fallback": CODEX_HOME / "skills" / "browser-harness" / "SKILL.md",
        "desktop_fallback": CODEX_HOME / "skills" / "desktop-control" / "SKILL.md",
        "web_access": CODEX_HOME / "skills" / "web-access" / "SKILL.md",
        "data_report": CODEX_HOME / "skills" / "data-analysis-report" / "SKILL.md",
        "playwright": CODEX_HOME / "skills" / "playwright" / "SKILL.md",
        "absorb_lessons": CODEX_HOME / "skills" / "absorb-lessons" / "SKILL.md",
        "adversarial_review": CODEX_HOME / "skills" / "adversarial-review" / "SKILL.md",
        "project_h5_audit": CODEX_HOME / "skills" / "project-prd-h5-audit" / "SKILL.md",
        "huashu": CODEX_HOME / "skills" / "huashu-design" / "SKILL.md",
        "open_design_systems": CODEX_HOME / "skills" / "open-design-design-systems" / "SKILL.md",
    }
    for label, path in paths.items():
        if not path.exists():
            failures.append(f"missing {label}: {path}")

    if failures:
        print(json.dumps({"checks": checks, "failures": failures}, ensure_ascii=False, indent=2))
        return 1

    texts = {label: read(path) for label, path in paths.items()}

    def require(label: str, condition: bool, message: str) -> None:
        if condition:
            checks.append(label)
        else:
            failures.append(f"{label}: {message}")

    require(
        "company_h5_is_scoped",
        "Use only for company/work H5" in texts["app_factory"]
        and "Do not use for generic, personal, client, open-source" in texts["app_factory"]
        and "default skill for all H5" not in texts["app_factory"],
        "app-factory still behaves as a global H5 default",
    )
    require(
        "company_h5_sequence",
        texts["app_factory"].find("Build the user-facing H5 prototype")
        < texts["app_factory"].find("blind black-box H5 walkthrough")
        < texts["app_factory"].find("define and build the admin prototype")
        < texts["app_factory"].find("write the PRD"),
        "expected H5 -> black-box -> admin -> PRD ordering is missing",
    )
    require(
        "generic_h5_uses_product_design",
        "For generic, personal, client, open-source" in texts["router"]
        and "use Product Design `index` as the primary route" in texts["router"]
        and "Do not select `app-factory-h5-admin`" in texts["router"],
        "generic H5 route is ambiguous or leaks company workflow",
    )
    require(
        "admin_gate_continues",
        "Continue, Do Not Stall" in texts["admin_gate"]
        and "## Hard Stop" not in texts["admin_gate"]
        and "default to Linear-like" not in texts["admin_gate"],
        "admin gate can still stop at planning or force one style",
    )
    require(
        "prd_questions_are_batched",
        "Ask one question at a time" not in texts["pm_prd"]
        and "one compact batch" in texts["pm_prd"],
        "pm-prd still creates one-question turns",
    )
    require(
        "agent_reach_reference_is_inert",
        frontmatter(paths["agent_reach_reference"]).get("name") == "agent-reach-upstream-reference"
        and "allow_implicit_invocation: false"
        in read(paths["agent_reach_reference"].parent / "agents" / "openai.yaml"),
        "upstream Agent Reach copy can still compete as a default router",
    )
    require(
        "legacy_names_are_narrow",
        frontmatter(paths["image_fallback"]).get("name") == "image-to-code-fallback"
        and frontmatter(paths["pdf_fallback"]).get("name") == "pdf-legacy-fallback"
        and frontmatter(paths["xlsx_fallback"]).get("name") == "xlsx-legacy-fallback"
        and frontmatter(paths["docx_fallback"]).get("name") == "docx-legacy-fallback"
        and frontmatter(paths["pptx_fallback"]).get("name") == "pptx-legacy-fallback"
        and frontmatter(paths["browser_fallback"]).get("name") == "browser-cdp-fallback"
        and frontmatter(paths["desktop_fallback"]).get("name") == "desktop-control-fallback",
        "legacy skills still collide with official plugin names",
    )
    for label in (
        "xlsx_fallback",
        "docx_fallback",
        "pptx_fallback",
        "browser_fallback",
        "desktop_fallback",
    ):
        policy_path = paths[label].parent / "agents" / "openai.yaml"
        require(
            f"{label}_implicit_disabled",
            policy_path.exists() and "allow_implicit_invocation: false" in read(policy_path),
            "legacy fallback can still trigger implicitly",
        )

    require(
        "web_router_owns_capability_order",
        "For GitHub repositories" in texts["web_access"]
        and "browser:control-in-app-browser" in texts["web_access"]
        and "For a local dev server" in texts["web_access"]
        and "browser-cdp-fallback" in texts["web_access"],
        "web-access does not distinguish GitHub, in-app Browser, Playwright, and CDP fallback",
    )
    require(
        "web_denials_are_route_scoped",
        "route-scoped" in texts["web_access"]
        and "permanent domain ban" in texts["web_access"]
        and "site-specific public reader" in texts["web_access"],
        "web-access can still turn one denied tool path into a permanent URL/domain failure",
    )
    require(
        "wechat_reader_is_executable",
        "setup_wechat_reader.ps1" in texts["agent_reach"]
        and "read_wechat_article.py" in texts["agent_reach"]
        and "debug-HTML recovery" in texts["agent_reach"],
        "agent-reach documents a WeChat route but does not own executable setup and recovery",
    )
    require(
        "dashboard_defers_to_data_analytics",
        "official Data Analytics" in texts["data_report"]
        and "does not own dashboard construction" in texts["data_report"]
        and "must not suppress the dashboard workflow" in texts["data_report"],
        "data-analysis-report can still swallow dashboard construction",
    )
    require(
        "playwright_is_not_generic_browser",
        "Do not select for ordinary public-page browsing" in texts["playwright"],
        "Playwright can still swallow generic public browsing",
    )
    require(
        "evolution_requires_impact_and_manifest",
        "Build an impact map" in texts["absorb_lessons"]
        and "Create a blind before/after test" in texts["absorb_lessons"]
        and "Produce a change manifest" in texts["absorb_lessons"],
        "self-evolution can still fix one example and omit exact change reporting",
    )
    require(
        "adversarial_modes_are_scoped",
        "Black-Box Walkthrough" in texts["adversarial_review"]
        and "Red-Team Plan Review" in texts["adversarial_review"]
        and "Do not manufacture objections to routine" in texts["adversarial_review"]
        and "route selection, static validation, artifact quality, and live behavior"
        in texts["adversarial_review"],
        "adversarial review is missing a mode, low-risk exclusion, or evidence-tier boundary",
    )
    require(
        "h5_requires_blind_live_evidence",
        "375px" in texts["app_factory"]
        and "findings report is frozen" in texts["app_factory"]
        and "cannot pass a readiness audit from source text and screenshots alone"
        in texts["project_h5_audit"],
        "H5 workflow can still pass without a blind live walkthrough",
    )
    require(
        "prd_red_team_is_conditional",
        "Red-Team Review" in texts["pm_prd"]
        and "Do not apply this gate to routine, reversible changes" in texts["pm_prd"],
        "pm-prd lacks a conditional red-team gate or can over-trigger on routine work",
    )
    require(
        "design_lanes_are_narrow",
        "Do not select for generic product planning" in texts["huashu"]
        and "Do not select merely because a UI should be beautiful" in texts["open_design_systems"],
        "Huashu or Open Design can still consume generic design requests",
    )

    local_names: dict[str, list[str]] = defaultdict(list)
    for root in (CODEX_HOME / "skills", AGENTS_HOME / "skills"):
        if not root.exists():
            continue
        for path in root.glob("*/SKILL.md"):
            name = frontmatter(path).get("name")
            if name:
                local_names[name.casefold()].append(str(path))
    duplicates = {name: rows for name, rows in local_names.items() if len(rows) > 1}
    require("no_global_local_name_collisions", not duplicates, f"duplicate names: {duplicates}")

    product_plugin = CODEX_HOME / "plugins" / "cache" / "openai-curated-remote" / "product-design"
    product_version = latest_version_dir(product_plugin)
    focused = {path.parent.name for path in (product_version / "skills").glob("*/SKILL.md")}
    referenced = {"index", "get-context", "ideate", "audit", "url-to-code", "image-to-code", "design-qa", "share"}
    require(
        "product_design_routes_exist",
        referenced <= focused,
        f"router references missing Product Design skills: {sorted(referenced - focused)}",
    )

    for label in (
        "router",
        "app_factory",
        "admin_gate",
        "pm_prd",
        "agent_reach",
        "adversarial_review",
        "project_h5_audit",
    ):
        lines = texts[label].count("\n") + 1
        require(f"{label}_context_budget", lines <= 500, f"{lines} lines exceeds 500-line budget")

    agents_path = CODEX_HOME / "AGENTS.md"
    if agents_path.exists():
        agents_lines = read(agents_path).count("\n") + 1
        require("global_agents_budget", agents_lines <= 260, f"AGENTS.md is {agents_lines} lines")

    skill_manifest = EXPORT_ROOT / "memories" / "vault_summaries" / "skill-change-manifest-2026-07-10.md"
    mechanism_manifest = (
        EXPORT_ROOT / "memories" / "vault_summaries" / "evolution-mechanism-manifest-2026-07-10.md"
    )
    correction_report = (
        EXPORT_ROOT / "memories" / "vault_summaries" / "gpt56-system-correction-2026-07-10.md"
    )
    projection_policy = (
        EXPORT_ROOT / "memories" / "vault_summaries" / "export-projection-policy.md"
    )
    sync_script = EXPORT_ROOT / "scripts" / "sync-codex-evolution.ps1"
    require(
        "skill_change_manifest_is_exact",
        skill_manifest.exists()
        and all(
            token in read(skill_manifest)
            for token in (
                "`absorb-lessons`",
                "`web-access`",
                "`ui-product-design-router`",
                "`data-analysis-report`",
                "`xlsx-legacy-fallback`",
                "`desktop-control-fallback`",
            )
        ),
        "system correction report omits exact changed-skill coverage",
    )
    require(
        "evolution_mechanism_manifest_is_tested",
        mechanism_manifest.exists()
        and all(
            token in read(mechanism_manifest)
            for token in (
                "map every affected",
                "failing baseline",
                "forces one worker",
                "degraded",
                "exact changed skills",
            )
        ),
        "evolution mechanism report omits intake, serial testing, or degraded-state rules",
    )
    require(
        "final_report_includes_behavioral_result",
        correction_report.exists()
        and "26/26 passed" in read(correction_report)
        and "explicitly degraded" in read(correction_report)
        and "34 active, 35 reference, and 8 candidate" in read(correction_report),
        "final report omits portfolio counts, behavioral tests, or degraded result",
    )
    require(
        "public_export_is_curated_projection",
        projection_policy.exists()
        and all(
            token in read(projection_policy)
            for token in (
                "not a byte-for-byte mirror",
                "Curated Projections",
                "Never run a recursive local-to-export copy",
                "check_export_safety.py",
            )
        ),
        "public export can still be treated as a raw local mirror",
    )
    require(
        "restore_preserves_private_skill_copies",
        sync_script.exists()
        and "curatedProjectionSkills" in read(sync_script)
        and "Preserved existing private-context skills" in read(sync_script),
        "restore script can still overwrite a private local skill with a public projection",
    )
    portability_check = EXPORT_ROOT / "tools" / "verify_portable_capabilities.ps1"
    denial_audit = EXPORT_ROOT / "tools" / "audit_access_denials.ps1"
    wechat_setup = EXPORT_ROOT / "skills" / "agent-reach" / "scripts" / "setup_wechat_reader.ps1"
    wechat_reader = EXPORT_ROOT / "skills" / "agent-reach" / "scripts" / "read_wechat_article.py"
    require(
        "restore_installs_and_tests_wechat_reader",
        all(path.exists() for path in (portability_check, denial_audit, wechat_setup, wechat_reader))
        and "setup_wechat_reader.ps1" in read(sync_script)
        and "verify_portable_capabilities.ps1" in read(sync_script)
        and "Live WeChat body extraction" in read(portability_check),
        "portable restore can still report success without installing or behaviorally testing the WeChat reader",
    )
    wechat_portability_report = (
        EXPORT_ROOT / "memories" / "vault_summaries" / "wechat-access-portability-2026-07-13.md"
    )
    require(
        "wechat_portability_failure_is_recorded",
        wechat_portability_report.exists()
        and "First fresh-install test failed" in read(wechat_portability_report)
        and "14,507-character body" in read(wechat_portability_report)
        and "Product safety policy is not bypassed" in read(wechat_portability_report),
        "WeChat portability correction omits failing baseline, live proof, or policy boundary",
    )
    operating_playbook = EXPORT_ROOT / "AI_OPERATING_PLAYBOOK.md"
    source_ledger = EXPORT_ROOT / "memories" / "self-evolution-ledger.md"
    bootstrap = EXPORT_ROOT / "BOOTSTRAP_AFTER_REINSTALL.md"
    readme = EXPORT_ROOT / "README.md"
    require(
        "portable_behavior_precedes_implementation",
        operating_playbook.exists()
        and all(
            token in read(operating_playbook)
            for token in (
                "No bundled script is required",
                "Capability Card: Public WeChat Article Reading",
                "Natural wording",
                "substantive article body text",
                "Route Ladder",
                "A Chrome/browser policy denial ends only that browser action or route",
                "equivalent target-runtime tools",
                "Evolution Admission Rule",
            )
        )
        and "source and decision audit, not the primary operating manual" in read(source_ledger)
        and "No-Code Behavior Restore" in read(bootstrap)
        and read(readme).find("AI_OPERATING_PLAYBOOK.md")
        < read(readme).find("memories/self-evolution-ledger.md")
        and "Write the portable operating card" in texts["absorb_lessons"],
        "export still depends on implementation scripts or leaves the ledger as the operating entry point",
    )
    safety_checker = EXPORT_ROOT / "tools" / "check_export_safety.py"
    require(
        "export_safety_checker_exists",
        safety_checker.exists()
        and "feishu_document_url" in read(safety_checker)
        and "personal_windows_path" in read(safety_checker)
        and '".jsonl"' in read(safety_checker)
        and "\\\\{1,2}" in read(safety_checker),
        "portable export lacks a fail-closed sensitive-value scanner",
    )
    weekly_sync = CODEX_HOME / "automations" / "weekly-evolution-sync" / "automation.toml"
    require(
        "weekly_sync_requires_safety_check",
        weekly_sync.exists()
        and "check_export_safety.py" in read(weekly_sync)
        and "hard stop" in read(weekly_sync)
        and "curated redacted projection" in read(weekly_sync)
        and "Never recursively overwrite" in read(weekly_sync),
        "weekly export sync can still stage unsafe files or overwrite curated projections",
    )

    print(
        json.dumps(
            {
                "checks_passed": len(checks),
                "failures": failures,
                "product_design_version": product_version.name,
                "local_skill_names": len(local_names),
                "duplicate_names": duplicates,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
