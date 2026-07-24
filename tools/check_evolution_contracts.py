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


def first_existing(*paths: Path) -> Path:
    return next((path for path in paths if path.exists()), paths[0])


def main() -> int:
    failures: list[str] = []
    checks: list[str] = []

    paths = {
        "router": CODEX_HOME / "skills" / "ui-product-design-router" / "SKILL.md",
        "app_factory": CODEX_HOME / "skills" / "app-factory-h5-admin" / "SKILL.md",
        "admin_gate": CODEX_HOME / "skills" / "admin-platform-execution-gate" / "SKILL.md",
        "pm_prd": CODEX_HOME / "skills" / "pm-prd" / "SKILL.md",
        "agent_reach": CODEX_HOME / "skills" / "agent-reach" / "SKILL.md",
        "agent_reach_reference": CODEX_HOME
        / "skill-archive"
        / "2026-07-15-zero-evidence"
        / "agent-reach-upstream-reference"
        / "SKILL.md",
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
        "project_h5_audit": first_existing(
            CODEX_HOME / "skills" / "project-prd-audit" / "SKILL.md",
            CODEX_HOME / "skills" / "project-prd-h5-audit" / "SKILL.md",
        ),
        "huashu": CODEX_HOME / "skills" / "huashu-design" / "SKILL.md",
        "open_design_systems": CODEX_HOME / "skills" / "open-design-design-systems" / "SKILL.md",
        "design_taste": CODEX_HOME / "skills" / "design-taste-frontend" / "SKILL.md",
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
        and "Run this skill only when the description's company scope is present"
        in texts["app_factory"]
        and "If the request is an unrelated H5, use the generic UI/product workflow"
        in texts["app_factory"],
        "app-factory still behaves as a global H5 default",
    )
    require(
        "company_h5_conditional_sequence",
        texts["app_factory"].find("Build the user-facing H5 prototype")
        < texts["app_factory"].find("blind black-box H5 walkthrough")
        < texts["app_factory"].find("Pause at the H5 review checkpoint")
        < texts["app_factory"].find("write the H5 PRD")
        and "Default scope is the user-facing H5 and its PRD" in texts["app_factory"]
        and "Enter this stage only when" in texts["app_factory"]
        and "If admin UI was explicitly requested, finalize the combined PRD after both H5 and admin confirmation"
        in texts["app_factory"],
        "expected H5 -> black-box -> H5 PRD default plus explicit-admin branch is missing",
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
        and "Ask no more than three concise questions, only after source inspection"
        in texts["pm_prd"],
        "pm-prd still creates one-question turns",
    )
    require(
        "agent_reach_reference_is_archived",
        frontmatter(paths["agent_reach_reference"]).get("name") == "agent-reach-upstream-reference"
        and "allow_implicit_invocation: false"
        in read(paths["agent_reach_reference"].parent / "agents" / "openai.yaml")
        and not (AGENTS_HOME / "skills" / "agent-reach").exists(),
        "upstream Agent Reach copy is missing from the archive or can still compete as a default router",
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
        "dashboard_prefers_official_with_labeled_fallback",
        "try official Data Analytics `index`" in texts["data_report"]
        and "Dashboard Degraded Fallback" in texts["data_report"]
        and "self-contained portable HTML dashboard" in texts["data_report"]
        and "must not suppress a callable dashboard workflow" in texts["data_report"],
        "dashboard fallback is missing, unlabeled, or can suppress callable official Data Analytics",
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
        and "开启对抗式审查" in texts["adversarial_review"]
        and "Separate known evidence, assumptions, and unknowns" in texts["adversarial_review"]
        and "Do not manufacture objections to routine" in texts["adversarial_review"]
        and "route selection, static validation, artifact quality, and live behavior"
        in texts["adversarial_review"],
        "adversarial review is missing a mode, low-risk exclusion, or evidence-tier boundary",
    )
    require(
        "h5_requires_blind_live_evidence",
        "375px" in texts["app_factory"]
        and "findings report is frozen" in texts["app_factory"]
        and "Static evidence can prove" in texts["project_h5_audit"]
        and "It cannot prove a runnable product works"
        in texts["project_h5_audit"],
        "H5 workflow can still pass without a blind live walkthrough",
    )
    require(
        "prd_avoids_universal_red_team_gate",
        "Red-Team Review" not in texts["pm_prd"]
        and "red-team" not in texts["pm_prd"].casefold(),
        "pm-prd duplicates the global conditional red-team rule or can over-trigger on routine work",
    )
    require(
        "design_lanes_are_narrow",
        "Do not select for generic product planning" in texts["huashu"]
        and "Do not select merely because a UI should be beautiful" in texts["open_design_systems"],
        "Huashu or Open Design can still consume generic design requests",
    )
    require(
        "design_lanes_require_real_artifacts",
        "functional controls under the same brief" in texts["router"]
        and "Method-description cards" in texts["router"]
        and "real task surfaces" in texts["router"],
        "multi-lane design can still pass from method cards, labels, or recolors",
    )
    require(
        "external_skill_sources_are_trackable",
        "https://github.com/bzd6661/wechat-article-for-ai" in texts["agent_reach"]
        and "upstream_tracking: head" in texts["agent_reach"]
        and "https://github.com/nexu-io/open-design" in texts["open_design_systems"]
        and "upstream_tracking: tag" in texts["open_design_systems"]
        and "https://github.com/Leonxlnx/taste-skill" in texts["design_taste"]
        and "upstream_policy: review_only" in texts["design_taste"],
        "active external adaptations can still disappear from update checks",
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
        agents_text = read(agents_path)
        agents_lines = agents_text.count("\n") + 1
        require(
            "global_agents_budget",
            agents_lines <= 40 and len(agents_text.encode("utf-8")) <= 4000,
            f"AGENTS.md is {agents_lines} lines and {len(agents_text.encode('utf-8'))} bytes",
        )
        require(
            "global_reasoning_and_commentary_are_scoped",
            "ambiguous, novel, or consequential decisions" in agents_text
            and "skip this overhead for routine reversible work" in agents_text
            and "Outside required progress updates" in agents_text
            and "do not narrate routine tool use" in agents_text
            and "material findings, decisions, blockers" in agents_text,
            "first-principles, adversarial, or commentary guidance is missing or globally over-broad",
        )

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
    automation_retention = EXPORT_ROOT / "tools" / "archive_old_automation_runs.py"
    automation_files = [
        CODEX_HOME / "automations" / automation_id / "automation.toml"
        for automation_id in ("automation", "metabase", "weekly-evolution-sync")
    ]
    require(
        "automation_run_retention_is_enabled",
        automation_retention.exists()
        and 'thread_source = \'automation\'' in read(automation_retention)
        and '[str(executable), "archive", session_id]' in read(automation_retention)
        and all(path.exists() and "archive_old_automation_runs.py" in read(path) for path in automation_files),
        "standalone automation runs can accumulate indefinitely or retention can bypass the supported archive command",
    )
    route_eval = EXPORT_ROOT / "tools" / "run_skill_route_evals.py"
    require(
        "route_eval_checks_continuation",
        route_eval.exists()
        and 'final_obj.get("would_continue_without_waiting") is not True' in read(route_eval),
        "route regression can still pass when the agent intends to stop between safe substeps",
    )
    require(
        "route_eval_is_bounded_and_incremental",
        "stdin=subprocess.DEVNULL" in read(route_eval)
        and "partial_report = build_report" in read(route_eval)
        and '"case_completed"' in read(route_eval),
        "route regression can still wait on stdin or lose completed cases during a later timeout",
    )
    require(
        "route_eval_report_is_portable",
        '"codex": f"codex.exe@{codex.parent.name}"' in read(route_eval)
        and '"codex": str(codex)' not in read(route_eval),
        "route regression reports can still leak a machine-specific executable path and block export sync",
    )
    audit_script = EXPORT_ROOT / "tools" / "audit_codex_system.py"
    require(
        "system_audit_classifies_expected_duplicates",
        audit_script.exists()
        and "plugin_scoped_duplicate_names" in read(audit_script)
        and "mirror_duplicate_groups" in read(audit_script)
        and "unexplained_duplicate_groups" in read(audit_script),
        "system audit can still report plugin namespaces or private mirrors as unresolved conflicts",
    )
    require(
        "system_audit_is_owner_aware",
        'row.root_kind == "codex-local" and not row.has_openai_yaml' in read(audit_script)
        and "owner_managed_without_openai_yaml" in read(audit_script),
        "system audit can still flag Lark or plugin-managed skills for missing Codex policy files",
    )
    skill_surface_validator = EXPORT_ROOT / "tools" / "validate_skill_surfaces.py"
    require(
        "skill_validation_is_owner_aware",
        skill_surface_validator.exists()
        and "run_codex_validation" in read(skill_surface_validator)
        and "run_lark_check" in read(skill_surface_validator)
        and '"version"' in read(skill_surface_validator)
        and '"skills_status"' in read(skill_surface_validator),
        "all skills can still be judged by one incompatible frontmatter validator",
    )
    external_update_checker = EXPORT_ROOT / "tools" / "check_external_skill_updates.py"
    require(
        "external_update_check_is_honest",
        external_update_checker.exists()
        and "needs_baseline" in read(external_update_checker)
        and "def head_ref" in read(external_update_checker)
        and "unsupported_tracking" in read(external_update_checker),
        "external update checks can still omit branch-only sources or unverified baselines",
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
