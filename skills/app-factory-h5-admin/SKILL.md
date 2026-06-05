---
name: app-factory-h5-admin
description: Use when the user asks for a new H5 project, H5 app factory, unified-admin new project, 声之境-style reuse, 每周穿搭-style adaptation, 750px H5 prototype, or a reusable H5 plus admin project package under the existing unified backend.
---

# H5 + Unified Admin App Factory

This skill turns one proven project pattern into repeatable new-product delivery. It is not a generic PRD writer. It must inspect the existing reference project and map reusable modules before producing artifacts.

Future projects are H5 only. Do not create non-H5 deliverables unless the user explicitly overrides this.

## Mandatory Companion Skills

- Use `pm-prd` for context-first intake and the PRD phase. In this app-factory workflow, do not produce the full PRD before the user has reviewed and confirmed the HTML prototypes, unless the user explicitly asks for PRD-first output.
- Use `admin-platform-execution-gate` and `open-design-design-systems` before backend/admin decomposition or backend/admin HTML. In this app-factory workflow, backend/admin work starts after the H5 core experience and H5 HTML have been reviewed, unless the user explicitly asks to design backend first.
- Use `wechat-pay-product-design` only when the new project includes WeChat Pay H5 payment, delegated deduction, subscriptions, orders, or merchant rollout.

## Source Gate

Before drafting or coding, inspect the relevant real sources:

1. Reference PRDs and mockups:
   - `D:\xiaochengxu\shengzhijing\声之境素材\方案\PRD-多应用管理平台.md`
   - `D:\xiaochengxu\shengzhijing\声之境素材\方案\mockup-多应用管理平台.html`
2. Reference H5/admin implementation:
   - `D:\xiaochengxu\shengzhijing\H5-MIGRATION-PLAN.md`
   - `D:\xiaochengxu\shengzhijing\h5-web`
   - `D:\xiaochengxu\shengzhijing\admin-web`
3. If implementation is requested, inspect current `h5-web`, `admin-web`, and CloudBase/cloudfunction files in the target workspace.
3. If the target project already has files, inspect them before creating new artifacts.

If these files are unavailable, say which source is missing and continue only with an explicit "source missing" assumption.

## Analysis And Question Gate

Do not start HTML immediately. First produce a compact analysis packet that makes the product shape reviewable:

```markdown
| Source | Must Inherit | Adapt For New Project | Must Not Copy | Open Questions |
|---|---|---|---|---|
```

Also lock:

- project name and one-sentence product job
- content modality: audio, image/text, video, checklist, article, product card, or mixed
- core user experience: what the user opens first, what they consume, what they decide, what they save/pay/share
- backend/admin implications hypothesis: what operators may need to create, review, publish, configure, audit, and measure; do not treat this as confirmed backend scope yet
- H5 page/function decomposition: user-facing pages, key states, and primary actions
- candidate backend/admin pages and functions to validate after H5 confirmation
- free/paid/subscription/payment boundary
- data model additions and fields to reuse
- H5 prototype width: default `750px` single-image/mobile-design width. Use `max-width: 750px; width: 100%; margin: 0 auto;` for responsive HTML.

If the core experience or function boundary is not confirmed, ask 1-3 high-impact questions and stop before HTML. Prefer a recommended assumption plus why it matters, not an empty menu of options. Continue to HTML only after the user answers, or after the user explicitly says to proceed with assumptions.

## Default Delivery Sequence

Analysis and questions come before HTML; H5 frontend comes before backend; backend confirmation comes before PRD. The app factory must converge the user-facing experience first because backend functions should be derived from the confirmed H5 behavior, not guessed in parallel.

1. **Source/context packet**
   - Inspect the source project and current unified-admin references.
   - Produce the compact inheritance/adaptation packet.
2. **Product decomposition and questions**
   - Summarize the proposed core H5 experience first.
   - Split functions into H5 user flows, content modules, payment/member boundary, and only a candidate backend/admin implication list.
   - Ask 1-3 necessary questions if the H5 experience or major business boundary is not confirmed.
   - Stop here if the answers materially change H5 pages, core functions, payment, data, or content operations.
3. **H5 frontend HTML phase**
   - Create the 750px H5 HTML prototype first.
   - The H5 HTML must expose user page structure, function boundaries, key states, primary actions, data fields, and navigation.
   - Verify the H5 prototype locally or in browser when possible.
4. **H5 confirmation gate**
   - Stop after H5 HTML and report: H5 prototype is ready for review; backend HTML and PRD have not been written yet.
   - Wait for the user to confirm H5 page/function direction or request changes.
   - Do not create backend/admin HTML from unconfirmed H5 screens.
5. **Backend/admin decomposition and questions**
   - Based on confirmed H5 behavior, derive backend/admin jobs: content creation, review/publish, configuration, orders/payment, users/permissions, metrics, audit, and operations.
   - Run the admin execution gate and lock page task matrix, primary actions, table/form/filter density, states, permissions, metrics, and screenshot review plan.
   - Ask 1-3 backend-specific questions if operator workflow, data ownership, payment/order handling, permissions, or metrics are not confirmed.
   - Stop here if answers materially change backend pages, admin functions, data model, or operational workflow.
6. **Backend/admin HTML phase**
   - Create the unified-admin HTML prototype after backend/admin scope is confirmed or explicitly assumed.
   - Verify admin density, table/detail/form states, and primary operations locally or in browser when possible.
7. **Backend confirmation gate**
   - Stop after backend HTML and report: backend prototype is ready for review; PRD has not been written yet.
   - Wait for the user to confirm backend/admin page/function direction or request changes.
8. **PRD phase**
   - After H5 and backend/admin confirmation, write the PRD against the confirmed HTML and context packet.
   - Reference the confirmed H5 and backend prototype filenames and accepted page/function scope.
   - If either prototype changes later, update the PRD only after syncing the changed HTML scope.

Bypass rule: if the user explicitly says to skip questions, write frontend/backend together, write backend first, or write PRD first, skip only the named gate and state that the normal gate is being bypassed.

## Reusable Product Skeleton

For each new project, map from the existing pattern instead of starting from a blank page:

| Layer | Existing Voice Project | Generic Module | Example: 每周穿搭 |
|---|---|---|---|
| App identity | 声之境 | app registry item | 每周穿搭 |
| Content unit | audio track | content item | weekly outfit issue / look card |
| Browsing | category tabs + content cards | category/filter + cards/list | season/style/weather/body-scene filters |
| Detail | player page | content detail page | image gallery + outfit rationale + item list |
| Access control | free/VIP audio | free/paid content gate | free preview + member-only full plan |
| Paywall | membership modal/page | purchase/upgrade flow | unlock weekly archive or premium outfit plan |
| Mine | membership status | account/benefits/settings | saved looks, member status, preferences |
| Admin content | audio upload/edit/list | content CRUD + status + ordering | image/text issue editor + tags + publish state |
| Admin config | pricing/switches | app-level config | membership price, publish cadence, category dictionaries |
| Orders | payment records | read-only order list | subscription/order history if paid |

## Required Deliverables

When the user asks for a new project package, do not stop after one artifact. Deliver the requested set in the sequence above:

1. Product decomposition packet
   - source inheritance table
   - core H5 experience
   - H5 page/function map
   - candidate backend/admin implications, not confirmed backend scope
   - 1-3 blocking questions or explicit assumptions
2. H5 HTML prototype after the decomposition gate
   - H5-only HTML prototype, default canvas/content width `750px`
   - multiple switchable screens, at minimum home/list, detail, paywall or upgrade state when relevant, and mine/account
   - no marketing landing page unless explicitly requested
3. H5 review packet
   - H5 page list and state list
   - confirmed H5 assumptions
   - H5 function/data boundaries visible in the HTML
   - open backend/admin implications
4. Backend/admin decomposition packet after H5 confirmation
   - operator jobs and page task matrix
   - content/data/payment/user/metrics/audit boundaries
   - 1-3 backend-specific blocking questions or explicit assumptions
5. Unified admin HTML prototype after backend decomposition
   - 1280px admin frame pattern, persistent left navigation around 220px
   - app overview, content management, create/edit drawer, config, order/payment page when applicable, account/permission surface when relevant
   - table/filter/detail/action states must be real-looking, not decorative cards
6. Backend review packet
   - backend page list and state list
   - confirmed backend assumptions
   - backend function/data boundaries visible in the HTML
   - open items that block PRD
7. PRD `.md` after H5 and backend HTML confirmation
   - overview, goals, non-goals, users, success metrics
   - content library and taxonomy
   - user stories with testable acceptance criteria
   - user-facing page structure matched to confirmed H5 HTML
   - admin/back-office requirements matched to confirmed backend HTML
   - data model and API/cloudfunction implications
   - edge cases and rollout plan
8. Module/data map
   - what reuses the unified platform
   - what is app-specific
   - what CloudBase collections/functions need adding or adapting
9. Verification
   - open HTML locally or in browser when possible
   - check mobile width, overflow, page switching, visible primary actions, and admin table density

## Output Discipline

- Start from the user's end goal and keep going through all required artifacts.
- For new H5 app-factory work, never claim the package is complete after only the context packet or only one prototype.
- Do not write HTML before the core experience and page/function boundary are analyzed and either confirmed by the user or explicitly assumed.
- Do not write backend/admin HTML in the same pass as H5 frontend HTML unless the user explicitly asks for simultaneous prototypes.
- Do not write backend/admin HTML before the H5 frontend prototype has been reviewed and confirmed, because backend functions must derive from confirmed H5 behavior.
- Do not write full PRD before both H5 and backend/admin HTML confirmation. If H5 is confirmed but backend is not, the correct status is "H5 confirmed; backend prototype pending; PRD pending backend confirmation."
- Do not ask step-by-step unless the next decision changes product direction, payment scope, account actions, or data risk.
- Do not copy the old project's content, pricing, merchant data, AppID, or secrets.
- Do not produce non-H5 pages, non-H5 payment assumptions, or narrow phone-frame prototypes by default.
- Treat source React files with encoding problems as structural references only; use PRD/mockup or new context for Chinese copy.
- If the result still looks like a generic CRUD/card pile, the skill failed; restart from the context packet and admin gate.

## References

- Read `references/shengzhijing-source-map.md` when using the source project.
- Read `references/reusable-module-map.md` when adapting a new app such as 每周穿搭.
