---
name: admin-platform-execution-gate
description: Use before building or revising admin platforms, internal tools, dashboards, back-office systems, multi-app management consoles, account/permission pages, monitoring consoles, or any backend UI where product positioning, information architecture, interaction quality, and visual execution must be correct before coding. Also trigger naturally when the user says an admin/internal UI is ugly, amateur, garbage, structurally wrong, not inheriting references, just small patches, page relationships are confused, metrics are nonsense, controls are fake, or installed design/planning skills had no effect.
---

# Admin Platform Execution Gate

This skill prevents a recurring failure mode: turning a platform/admin request into a pile of runnable features without first locking the product structure, page tasks, interaction rules, and visual acceptance criteria.

## When To Trigger

Use this before code or UI edits when the request involves:

- Internal tools platform, multi-app/app management platform, admin console, backend, CRM, operations dashboard, monitoring console, permission/account management, payment/customer/merchant tooling.
- A user says to reference a PRD, HTML prototype, prior platform, design system, or existing admin product.
- The user criticizes a backend as ugly, fake, unstructured, not inherited from references, or not thinking through page relationships.
- Natural-language complaints count. The user does not need to say "trigger admin gate" or name this skill. Phrases like "丑", "垃圾", "像新人", "没审美", "页面关系不对", "又是小改", "没继承参考", "指标没脑子", "按钮是假的吗", "skill 没用上", or "先别改, 让我看你准备怎么做" are enough to trigger this gate for admin/internal products.

## Hard Stop

Do not start implementation until the gate artifacts below are produced or updated. If existing code is already bad, do not keep patching page by page; first re-establish the gate, then edit.

## Template-First Rule

For admin/internal UI redesign after a quality failure, do not start from a blank page or from the broken project page. Start by copying and adapting `assets/admin-console-reference.html`, then replace content, data, routes, and product-specific labels. This is intentionally closer to using a good skill output as scaffolding than trusting freehand taste.

Run `python scripts/validate_admin_template.py` from this skill directory when changing the template. For project work, the adapted page must preserve the template's mature console structure unless a better inspected reference is explicitly chosen.

## Redesign Loop Breaker

If the user has rejected the admin UI twice, says the whole platform feels wrong, says prior design/planning skills had no effect, or asks to see the intended redesign before more edits, stop incremental patching.

Before touching project code again, produce a reset packet:

- current failure inventory, grouped by product positioning, navigation/page model, metric logic, interaction state, visual system, and verification gap
- the new platform model in one sentence, including who uses it and what decision the first screen must support
- reference inheritance packet and page task matrix updated from actual source PRD/HTML or product references
- one proposed visual/system direction with concrete tokens
- either an isolated review artifact (static HTML, screenshot, or mockup) or a clear statement of why the project must be edited directly

Do not treat screenshots, successful builds, or "I opened the skill" as sufficient. The loop is broken only when the next output changes the platform structure and decision model, not just colors, spacing, or another small patch.

## Reference-Grade Execution Contract

For internal-tool/admin redesigns, the next artifact must look and behave like a real mature console, not a dressed-up debug page. Apply these defaults unless the inspected reference proves a better choice:

- App shell: persistent left navigation 220-260px, top bar 56-64px, full-width work area. Do not leave large unused columns or put the real work in a narrow right-side strip.
- Navigation model: group by user job and product hierarchy, not by implementation tables. A detail view belongs under its parent workflow unless it is a separate recurring job.
- First screen: answer one operator decision in the first viewport. Use 3-5 decision metrics maximum, each tied to a next action. No decorative overview cards.
- Table density: admin tables use 40-48px rows, sticky header, visible key diagnostic fields, inline status chips, filter/search toolbar, and a detail drawer or split pane for long evidence.
- Detail pattern: use a drawer, split pane, or dedicated drill-in page. Do not duplicate the same entity as "selected batch result" and "product detail search" unless users truly need two different jobs.
- Actions: every visible action is implemented, disabled with a reason, or explicitly labeled as unavailable. One primary action per screen.
- Forms: create/edit flows use drawer/modal/dedicated form route, not permanent crowded forms next to the main list unless the product is explicitly a form tool.
- Metrics: reject "yesterday", "finished", "recent records", or raw counts unless they answer a business question. Prefer latest full-run result, affected products, unresolved failures, alert delivery, freshness, and owner/action state.
- Visual system: 12/14/16px UI type, restrained palette, 6-8px radius, low-noise borders, one accent color, clear hover/focus/disabled/loading/empty/error states. No hero sections, marketing cards, random gradients, oversized headings, or repeated card grids for dense operations work.
- Evidence: before finalizing, compare the screenshot against the chosen reference system and state what was inherited. If it still looks like a beginner CRUD page, it is not done.

## Required Gate Artifacts

### 1. Reference Inheritance Packet

Create a compact packet from the referenced PRD/prototype/product:

```markdown
| Source | Must Inherit | Adapt For This Project | Must Not Copy | Open Questions |
|---|---|---|---|---|
```

Do not treat references as visual decoration. Extract page relationships, permission model, primary workflows, information hierarchy, and interaction patterns.

### 2. Page Task Matrix

Before UI work, define every page:

```markdown
| Page | User | Primary Job | Primary Action | Secondary Actions | Information Priority | Must Not Show |
|---|---|---|---|---|---|---|
```

Rules:
- Each page has one primary action at most.
- Do not split pages unless users have different jobs or decision moments.
- Do not merge pages if doing so hides a critical workflow or creates a noisy table.

### 3. Business Metric Gate

Every metric on a dashboard must answer a decision question.

Reject metrics like:
- raw technical status such as `finished` when it does not help the operator
- arbitrary day metrics such as yesterday pass rate unless the business explicitly compares days
- repeated recent rows that make product-level status look duplicated

Prefer:
- latest full-run pass rate
- latest abnormal count
- affected products in latest run
- completion time only when freshness matters
- trend only as secondary context

### 4. Interaction Gate

Block the edit if any of these are true:

- A visible button has no implemented behavior and is not explicitly marked as unavailable.
- A page has duplicate primary actions such as two "new/create" controls.
- A table truncates fields needed for diagnosis, such as failure reason, exception detail, payment URL, webhook error, or screenshot path.
- Create/edit forms permanently crowd the main list when a drawer, detail pane, or clearly scoped form region is the expected pattern.
- Run-level records and result-level records are separated without a user/job reason.

### 5. Visual Gate

Before coding visual UI, choose a real design-system benchmark and convert it into tokens:

- palette and surface levels
- typography scale and weights
- spacing and density
- border radius and borders
- table density
- button hierarchy
- status colors
- empty/loading/error states

For dense SaaS/internal tooling, default to Linear-like restraint: dark-native surfaces, low-noise borders, one accent color, compact tables, clear navigation, no decorative hero treatment.

## Verification Before Completion

Do not claim completion from build success alone. Verify with browser screenshots and inspect:

- The first screen answers the user's main decision.
- Page titles are not repeated incoherently.
- Each page has at most one primary action.
- Buttons shown on the screen can actually be used.
- Diagnostic fields are readable without hover-only or ellipsis-only access.
- Navigation matches the platform/app/tool hierarchy.
- The screenshot looks like a real long-term admin product, not a temporary debug panel.

If any check fails, fix before reporting completion.
