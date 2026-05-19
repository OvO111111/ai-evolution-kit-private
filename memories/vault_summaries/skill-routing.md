---
page_type: topic
created_at: "2026-05-18"
updated_at: "2026-05-18"
sensitivity: personal
source_ids: ["skill_routing_audit", "memory_registry"]
confidence: high
status: active
---

# Skill Routing

## Default Rule

Use the smallest matching tool set. Do not stack overlapping skills just because they exist.

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
