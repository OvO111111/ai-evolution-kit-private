---
name: app-factory-h5-admin
description: Use only for company/work H5 products that reuse the established unified-admin factory, including explicit references to 声之境, 每周穿搭, 自营产品管理平台, 统一后台, the company H5 factory, matching company workspace paths, or an explicit request to reuse that project family. Covers staged product analysis, conditional red-team review, a 750px H5 review artifact, blind H5/operator black-box walkthroughs, modular unified-admin reuse, and PRD generation after prototypes are confirmed. Do not use for generic, personal, client, open-source, or unrelated H5 work.
---

# Company H5 And Unified Admin Factory

This is a project-derived workflow. Its product facts and reusable modules belong only to the matching company project family.

## Scope Gate

Run this skill only when the description's company scope is present. If the request is an unrelated H5, use the generic UI/product workflow and current project rules.

Before reusing an old project, separate:

- reusable product pattern;
- reusable admin module;
- target-project facts that must be inspected again;
- old IDs, prices, legal subjects, payment data, and content that must never be copied by default.

## Stage Order

The default sequence is deliberate:

1. Inspect sources and establish the product model.
2. Resolve blocking questions in one compact batch.
3. Red-team the direction only when material product, payment, compliance, dependency, or operating assumptions remain.
4. Build the user-facing H5 prototype.
5. Run a blind black-box H5 walkthrough, fix verified defects, and rerun the same journeys.
6. Pause at the H5 review checkpoint.
7. After H5 confirmation, define and build the admin prototype.
8. Run a blind operator black-box walkthrough, fix verified defects, and rerun the same journeys.
9. Pause at the admin review checkpoint.
10. After both prototypes are confirmed, write the PRD against those artifacts.

Do not write the full PRD before the page and function direction is confirmed. Do not build the admin before the user-facing H5 has established what operators need to manage. Within each stage, continue through the obvious work and verification; do not stop after every substep.

If the user explicitly asks for an end-to-end draft without review pauses, produce all stages with clearly marked assumptions, but still keep the dependency order.

## Stage 1: Source And Product Model

Inspect the current target project plus the relevant source project. Read `references/shengzhijing-source-map.md` and `references/reusable-module-map.md` only when those sources match the task.

Produce a compact working packet:

| Source | Must inherit | Adapt for target | Must not copy | Open question |
|---|---|---|---|---|

Lock these decisions before HTML:

- target user and one-sentence product job;
- core experience from entry to completion;
- page list, primary action, navigation, and key states;
- content model and what is generated, configured, or uploaded;
- free, paid, membership, subscription, order, payment, and agreement boundaries where applicable;
- admin implications, permissions, audit trail, and operational owner;
- explicit non-goals for the current release.

Ask no more than three high-impact questions in one batch, and only when their answers materially change the experience, payment/compliance, data ownership, or admin scope. If sources answer them, proceed without asking.

Before HTML, use `adversarial-review` in red-team mode only when the proposed direction depends on an unverified high-cost assumption, new external dependency, payment/compliance interpretation, difficult-to-reverse data model, or repeated operating burden. Require a minimum falsification experiment before committing to such an assumption. Do not slow ordinary reuse work with ceremonial red-team output.

## Stage 2: H5 Prototype

The design/review canvas is 750px wide. The HTML must remain responsive on a real phone viewport:

```css
.h5-canvas {
  width: min(100%, 750px);
  margin: 0 auto;
}
```

Use 750px for single-page review images and design handoff. Do not confuse the 750px design canvas with the physical CSS viewport of a 375px phone.

Build the complete user-facing stage, including the states required by the confirmed product model. Do not add membership, payment, agreements, customer service, orders, or review materials merely because another company H5 had them; include them only when current sources or the user require them.

Verify:

- all H5 pages and routes open;
- first viewport communicates the main job and primary action;
- mobile layout has no overflow or overlap;
- controls and navigation work;
- empty, loading, error, long-content, and payment/result states exist when applicable;
- screenshots cover the main flow, not only the home page.

After implementation checks, use `adversarial-review` in black-box mode before the H5 review checkpoint. Give the evaluator only the user goal, runnable target, critical journeys, permitted test data, and action boundaries. Do not expose source code, implementation notes, known defects, or intended fixes until the first findings report is frozen. Test on a real `375px` or `390px` CSS viewport; the `750px` canvas remains a review/handoff artifact only. If defects are fixed, rerun the exact same journeys before asking the user to confirm the H5.

Then report the H5 artifact for the explicit review checkpoint. Do not silently continue into the PRD.

## Stage 3: Unified Admin

After H5 confirmation, derive the operator workflow from the accepted H5 and content/data model.

Use `admin-platform-execution-gate` before admin implementation. Prefer reusable modules from `references/reusable-module-map.md`, but revalidate every field, state, permission, metric, and action for the target project.

Define:

| Page/module | Operator job | Managed entity | Primary action | Key states | Permission/audit need |
|---|---|---|---|---|---|

The admin must manage the actual H5 behavior. Avoid decorative dashboards, meaningless totals, duplicated pages, and fake controls. Verify the full operator flow and responsive desktop layout, then stop at the admin review checkpoint.

Before that checkpoint, run `adversarial-review` in black-box mode as a first-time operator. Exercise the real create/configure/publish/revoke or equivalent workflow, permission boundaries, empty/error states, destructive confirmations, and whether changes are reflected in the accepted H5 behavior. Freeze findings before implementation inspection; after fixes, rerun the same operator journeys.

## Stage 4: PRD

After H5 and admin confirmation, use `pm-prd` to write the PRD. The PRD must cite the confirmed prototype filenames and describe the accepted behavior, not an earlier assumption.

Include:

- user and operator flows;
- page/function inventory;
- module reuse and target-specific adaptations;
- entities, states, roles, permissions, and audit needs;
- requirements with stable IDs and testable acceptance criteria;
- non-goals, dependencies, rollout, analytics, and operational handoff;
- unresolved decisions only when they remain genuinely unresolved.

## Paid Company H5

Read `references/paid-h5-subscription-package.md` only for a matching paid/self-operated company H5. Treat its package table as a project-family reference, not a global truth.

Before using package or legal facts, verify the current source of truth for price, cycle, renewal, benefits, refund/cancel language, merchant display name, company subject, customer service, agreements, and review requirements. Never copy AppIDs, env IDs, merchant IDs, customer data, or payment credentials from an old project.

## Completion

The workflow is complete only when the stage requested by the user is delivered and verified. A source packet, one HTML file, or a build command is not completion for an end-to-end request.
