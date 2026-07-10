---
name: admin-platform-execution-gate
description: "Use before building or revising admin platforms, internal tools, dashboards, back-office systems, CRMs, approval systems, multi-app consoles, permissions/account pages, monitoring consoles, or payment/customer/merchant operations UIs. Also use when an admin UI is described as ugly, amateur, generic, structurally wrong, card-heavy, reference-blind, full of fake controls, or repeatedly patched without improvement. This is an execution gate: establish the product and design contract, then continue into the requested implementation in the same stage."
---

# Admin Platform Execution Gate

This gate prevents a technically runnable CRUD page from being mistaken for a usable operational product.

## Continue, Do Not Stall

Create the gate artifacts compactly, use them to guide the work, and continue into implementation in the same turn. Pause only when a missing decision materially changes product direction, permissions, sensitive data, production state, or cost.

Do not turn the gate into a long questionnaire or report completion after producing only matrices.

## 1. Product Model

State in one sentence:

- who operates the system;
- what decision or recurring job the first screen supports;
- what entity/workflow the platform owns;
- what outcome marks success.

If this cannot be grounded in supplied PRDs, current code, data, screenshots, or a named reference, inspect those sources before designing.

## 2. Reference Inheritance

Choose the closest real product or supplied reference by workflow fit, not by fashionable visual adjectives.

| Source | Inherit | Adapt | Do not copy | Evidence |
|---|---|---|---|---|

Extract navigation hierarchy, page relationships, table/detail behavior, permissions, status model, interaction states, density, typography, and component rules.

`assets/admin-console-reference.html` is an optional scaffold for a matching dense operations console. Do not use it when another inspected reference is a better fit, and do not force every admin product into the same shell, palette, or composition.

## 3. Page Task Matrix

| Page | User job | Primary decision/action | Secondary actions | Information priority | Must not show |
|---|---|---|---|---|---|

Rules:

- group navigation by operator job and product hierarchy, not database tables;
- give each screen one primary action at most;
- use a drawer, split pane, or dedicated detail route according to task depth;
- do not duplicate the same entity across pages unless the user jobs are genuinely different;
- dashboard metrics must lead to an operator decision or action.

## 4. Data, Permission, And State Contract

For each managed entity, define lifecycle states, important fields, owner, permission boundary, audit events, and failure/recovery behavior.

Visible actions must be functional, disabled with a reason, or explicitly unavailable. Include loading, empty, error, partial-data, long-content, permission-denied, and stale-data states where relevant.

## 5. Visual System

Derive tokens from the selected reference and domain:

- type scale and density;
- surfaces, borders, and elevation;
- spacing and layout tracks;
- table row height and column priority;
- button hierarchy and form behavior;
- status, warning, and error semantics;
- desktop and narrow-screen behavior.

Do not default every product to dark Linear-like styling. Do not use marketing heroes, oversized headings, decorative card grids, nested cards, random gradients, or large unused columns for operational tools.

## Rejection Reset

If the user has rejected the UI twice or says the whole structure is wrong, stop incremental CSS patching. In the same turn:

1. audit failures by product model, information architecture, metrics, interaction, visual system, and verification;
2. select a new reference family;
3. revise the page task matrix;
4. produce one isolated representative screen or direction artifact;
5. implement the accepted/reset direction across the affected surface when the request authorizes it.

A reset must change the decision model or structure, not only colors and spacing.

## Multi-Option Designs

When several design options are requested, hold business facts constant but vary at least four of: navigation, information architecture, primary interaction, composition, density, typography, color system, content hierarchy, and state presentation.

One template with recolors is not multiple options. Record each lane's reference and design thesis.

## Verification

Before completion:

- run the project checks;
- capture representative screenshots at desktop and narrow widths;
- inspect first viewport, navigation, table/detail flow, forms, long content, and major states;
- click every visible primary action and a representative set of secondary actions;
- compare the rendered result against the selected reference and page task matrix;
- fix overlap, clipping, dead controls, meaningless metrics, and incoherent page relationships.

If the artifact still looks like a dressed-up debug page or beginner CRUD template, it does not pass.
