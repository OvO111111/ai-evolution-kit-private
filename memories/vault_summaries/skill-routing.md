---
page_type: topic
created_at: "2026-05-18"
updated_at: "2026-05-19"
sensitivity: personal
source_ids: ["skill_routing_audit", "memory_registry"]
confidence: high
status: active
---

# Skill Routing

## Default Rule

Use the smallest matching tool set. Do not stack overlapping skills just because they exist.

Before any non-trivial task, run a skill gate:

- classify the task family
- name the selected skill(s), or state why no skill applies
- identify required source inspection before drafting or editing
- stop if a mandatory skill has not been opened or applied

For tasks involving existing artifacts, source inspection is part of the gate. It is not optional follow-up work.

## Current Routing Order

1. Structured local tools for files, docs, spreadsheets, slides, databases, and known local workflows.
2. `web-access` for general search, fetch, browser, and web routing.
3. `agent-reach` for public/social/video/article sources where site-specific tooling helps.
4. `browser-harness` for rendered pages, login-state pages, and CDP-style browser validation.
5. `desktop-control` only for non-browser desktop apps or explicit computer-control tasks.

## Known Overlap Zones

- `web-access` vs `agent-reach` vs `browser-harness`
- frontend rules vs `open-design-*`
- `absorb-lessons` vs self-improving-agent / SkillClaw style ideas
- `caveman*` vs normal communication
- project-specific tools vs global skills

## Mandatory Trigger Families

- PRD, product plan, solution plan, backend/admin prototype, grey-release decision system, or proposal + prototype tasks: use `pm-prd` and inspect referenced PRDs, HTML mockups, samples, interface docs, workflows, and confirmed business boundaries before drafting.
- Backend/admin UI, dashboards, internal tools, CRMs, approval systems, payment/customer-data consoles, or admin prototypes: use `open-design-design-systems`, pick the closest reference system first, and do not style from generic adjectives.
- Data analysis reports, Excel/CSV analysis, KPI/trend/comparison/cohort/root-cause reports, visualized HTML reports, Word/PPT analysis reports, or "analysis is not professional enough" feedback: use `data-analysis-report` first, then supporting file-format skills such as `xlsx`, `docx`, `pptx`, or `ocr-and-documents`.
- Self-evolution, external lessons, skill/rule updates, or "make Codex smarter" tasks: use `absorb-lessons`, log source + decision + validation.
- WeChat public article or difficult public/social web sources: route through `web-access`; use browser or the executable `agent-reach` Camoufox wrapper when static fetch fails. Require title plus substantive body extraction. A denied fetch/browser action is route-scoped and must not become a permanent URL/domain ban.
- WeChat work-group context: use `wechat-work-context`, keep groups isolated, read-only, and cite source messages.
- Feishu/Lark tasks: use the relevant Lark skill and edit the real Feishu surface, not a detached substitute.

## Validation Rule

When two skills overlap and the cost is reasonable, propose an A/B comparison tied to a real task. Do not install or benchmark every candidate immediately when there is no task pressure.

## EvoSkill-Inspired Governance

The current skill surface is already large enough that more skills can reduce judgment quality. Treat skill count as a cost.

Use these tiers:

- `active`: small set of frequently used, validated, high-signal skills.
- `reference`: installed or cloned for lookup, but not default-routed.
- `candidate`: potentially useful but unvalidated; needs a real benchmark task.
- `deprecated`: duplicated, stale, narrow one-off, or harmful to routing.

Admission rule:

- Do not create a new skill if editing an existing skill solves the failure.
- Do not keep a skill just because it was useful once.
- Do not let overlapping skills share the same default trigger unless one is clearly the router and the others are references.
- A skill should remain active only if it improves a realistic task, avoids repeated errors, or provides an executable tool path unavailable elsewhere.

Eviction rule:

- If a skill overlaps another and has no unique trigger/use case, demote it to reference or merge it.
- If a skill causes wrong routing twice, rewrite its description or demote it.
- If a skill has not been used or validated and only adds noise, keep it out of active routing.

Benchmark rule:

- Use task families, not single examples: web/article access, browser login tasks, document/OCR, PRD/solution planning, frontend/design, Feishu/Lark work, WeChat work context, payment product guidance, and export/memory retrieval.
- Keep a history of rejected proposals so the same bad skill idea is not re-added later.
