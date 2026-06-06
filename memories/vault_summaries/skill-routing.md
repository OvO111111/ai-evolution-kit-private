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

The skill gate must leave evidence. A mandatory skill is not considered applied unless its `SKILL.md` was actually opened in the current task or its concrete tool/script was used. Mentioning the skill name, relying on memory, or having the skill installed is not enough.

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

## Scope Boundary

Project-derived memories and skills are evidence for their project family, not global defaults. Before applying a project-derived rule, identify whether the request is:

- `global`: Codex behavior, skill governance, reporting discipline, verification, routing hygiene;
- `company/work`: 声之境, unified admin, 每周穿搭, WeChat work context, payment rollout, Feishu operations, customer/complaint/payment data;
- `personal/reusable`: user style preferences and general engineering habits that do not depend on a company source;
- `task-local`: facts only relevant to the current workspace.

Company/work memories may be used only when the task names that project/domain/workspace or clearly asks to reuse that company pattern. Generic H5, PRD, frontend, admin, or design tasks must not inherit company-specific constraints unless the user says so.

## Mandatory Trigger Families

- PRD, product plan, solution plan, backend/admin prototype, grey-release decision system, or proposal + prototype tasks: use `pm-prd` and inspect referenced PRDs, HTML mockups, samples, interface docs, workflows, and confirmed business boundaries before drafting.
- Company/work H5 app-factory projects under the existing unified admin platform, especially when the user references 声之境, 多应用管理平台, 统一后台, 每周穿搭, `D:\xiaochengxu\shengzhijing`, or explicitly asks to reuse the company app-factory pattern with 750px H5 HTML + unified-admin HTML + PRD/module map outputs: use `app-factory-h5-admin` first, then `pm-prd`, `admin-platform-execution-gate`, and `open-design-design-systems` as required. The skill must produce a source inheritance/context packet before drafting artifacts. Do not trigger this skill for unrelated personal projects, open-source projects, generic H5 work, or generic landing pages.
- Public-facing frontend, landing pages, portfolio/brand pages, visually important website redesigns, or image-first website work: use Taste routing. Use `design-taste-frontend` for new public pages, `redesign-existing-projects` for existing UI polish, and `image-to-code` when generated/reference images should drive the implementation.
- Backend/admin UI, dashboards, internal tools, CRMs, approval systems, payment/customer-data consoles, or admin prototypes: use both `admin-platform-execution-gate` and `open-design-design-systems`, pick the closest reference system first, and do not style from generic adjectives. This is a stop condition: before coding or reporting completion, lock selected reference, page task matrix, primary action, table/form/filter density, status/error/empty/loading states, metric definitions, permission/audit behavior, responsive behavior, and screenshot review plan.
- Backend/admin UI that has already been rejected twice, or where the user says the whole platform is ugly, structurally wrong, not using the installed skills, or only receiving small patches: trigger a redesign loop breaker. Stop project-code edits, produce a reset packet and an isolated review artifact or explicit before-code plan, then continue only after the platform model, IA, metric logic, interaction state, and visual tokens have been reset. Opening a skill is evidence of routing, not evidence of successful absorption.
- The user must not need to say the rule name. Natural complaints such as "丑", "垃圾", "像新人", "没审美", "页面关系不对", "小改没用", "没继承参考", "指标没脑子", "按钮是假的吗", "skill 没用上", or "先别改, 让我看方案" are sufficient trigger evidence for admin/internal products.
- For admin/internal redesigns, skill application is judged by concrete product patterns, not by naming a design system or changing visual tokens. The artifact must show app shell proportions, navigation model, first-screen decision, 3-5 decision metrics, table density, filter/search toolbar, detail drawer or split-pane, action states, empty/error/loading states, and explicit "must not show" decisions. A CRUD/card pile with better colors fails the route.
- Data analysis reports, Excel/CSV analysis, KPI/trend/comparison/cohort/root-cause reports, visualized HTML reports, Word/PPT analysis reports, or "analysis is not professional enough" feedback: use `data-analysis-report` first, then supporting file-format skills such as `xlsx`, `docx`, `pptx`, or `ocr-and-documents`.
- Self-evolution, external lessons, skill/rule updates, or "make Codex smarter" tasks: use `absorb-lessons`, log source + decision + validation.
- WeChat public article or difficult public/social web sources: route through `web-access`; use `agent-reach` or browser fallback when static fetch fails.
- WeChat work-group context: use `wechat-work-context`, keep groups isolated, read-only, and cite source messages.
- Feishu/Lark tasks: use the relevant Lark skill and edit the real Feishu surface, not a detached substitute.

## Validation Rule

When two skills overlap and the cost is reasonable, propose an A/B comparison tied to a real task. Do not install or benchmark every candidate immediately when there is no task pressure.

Run a usage audit when the user questions whether skills are really being triggered:

```powershell
python tools\audit_skill_usage.py
python tools\check_skill_routing.py
```

Audit result from 2026-05-28: 66 discovered skills, 32 active, 10 active skills with zero strong/assistant evidence, and 29 skills with zero evidence. The failure class is global routing enforcement, not a single design skill. Active-zero skills require one explicit disposition: demote, add/repair a trigger test, or mark as cold-active with a specific future trigger.

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
- A newly installed or promoted skill starts as unproven until there is strong evidence: current-task `SKILL.md` read, tool/script execution, route test, or realistic task validation.

Eviction rule:

- If a skill overlaps another and has no unique trigger/use case, demote it to reference or merge it.
- If a skill causes wrong routing twice, rewrite its description or demote it.
- If a skill has not been used or validated and only adds noise, keep it out of active routing.
- If a mandatory design skill is skipped and the output is ugly, structurally weak, or unverified, treat that as routing failure, not design taste preference. Patch the routing gate and add a trigger test before discussing more candidate tools.

Benchmark rule:

- Use task families, not single examples: web/article access, browser login tasks, document/OCR, PRD/solution planning, frontend/design, Feishu/Lark work, WeChat work context, payment product guidance, and export/memory retrieval.
- Keep a history of rejected proposals so the same bad skill idea is not re-added later.
