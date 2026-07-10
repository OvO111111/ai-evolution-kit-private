# Project PRD/H5 Audit Checklists

Use these checklists as audit criteria. They are not templates for writing new PRDs.

## Classification

Classify before auditing:

| Type | Use When | Main Risk |
|---|---|---|
| `refund_h5` | Branded refund query/application H5 | Wrong refund page semantics, wrong merchant facts, exposing internal reasons |
| `paid_self_operated_h5` | Company self-operated member/payment/subscription H5 | Wrong price model, stale subject, missing agreements/orders/subscriptions |
| `paid_partner_h5` | Externally branded or partner paid H5 | Reusing self-operated defaults incorrectly |
| `platform_or_admin` | Admin/backend/internal tool/platform | Treating code delivery as static HTML/PRD or splitting platform sub-tools |
| `handoff_package` | Project includes zip/package/assets/API/runtime docs | Missing non-PRD assets needed for development |

If type is unclear, ask. Do not apply self-operated defaults to partner projects.

## Universal Source Checks

- Official project name matches the user-confirmed current name.
- One independent product/system/H5/platform has one archive row.
- Similar projects are not merged unless the source or user confirms a merge.
- For a named-project audit, Feishu is only one possible source. If no Feishu archive exists, inspect local sources and report `source: local only`; do not mark it as a failure unless the task is specifically sync/archive-state checking.
- PRD and HTML are both present when expected.
- HTML is attached and previewed when synced to Feishu.
- Support materials are included when present: screenshots, price list, product intro, process flow, review material, API contract, runtime rules, template JSON, source list, asset manifest, zip package.
- Feishu archive tables that claim attached screenshots/files must be checked against current local source files, package entries, or Feishu attachments.
- Feishu-generated image descriptions/alt text must not be treated as source truth. If they contradict source files or images, flag the contradiction and verify the actual image.
- Feishu share permission should be link-readable when syncing is part of the task.
- Process candidates and HTML-only drafts stay out of formal navigation.

## Feishu Archive Wrapper Checks

Feishu project archives often contain operational metadata. That metadata is useful for traceability, but it should not be the first thing a developer, reviewer, or coworker has to read before the product itself.

Flag as issue when these sections appear before the actual PRD/product summary:

- `同步时间`
- `同步结论`
- `归档信息`
- `已附截图`
- `已附文件`
- source file timestamp tables
- long attachment byte-size tables

Expected structure:

- First screen should start with the product/project name and the actionable current status: what this product is, what is ready, what is missing, what must be built or reviewed.
- Archive metadata should be moved to `附件与来源`, `同步记录`, or `审计证据` after the main PRD/handoff content.
- Attachment tables should be compact. List only reader-relevant files by purpose, not byte sizes and mechanical sync details unless doing a sync audit.
- If the document is specifically a sync audit report, archive metadata can be first, but the title and conclusion must make that clear.

Flag as P1/P2:

- `P1`: shareable PRD opens with sync scaffolding and hides the actual product requirements.
- `P2`: archive metadata is useful but too verbose, duplicated, or placed before the reader's main task.

## PRD Information Density Checks

Flag as issue when PRD content consumes space without helping product, design, development, review, payment, legal, or operation decisions.

Low-value sections to challenge:

- Long product-positioning paragraphs that do not define page behavior, user-visible copy, data fields, benefits, package rules, or acceptance criteria.
- Generic user-value or goal statements that could fit any H5.
- "Background", "principle", "vision", "strategy", or "why we do it" text after the real decision has already been made.
- "本期不包含 / 非目标 / 暂不支持" lists that enumerate unrelated capabilities, competitor features, or obvious non-features.
- Repeated explanations of the same boundary across PRD, review material, and acceptance criteria.

Keep exclusions only when they prevent a likely mistake:

- A module looks likely by product category but must not be built, such as "album product has no upload flow" or "outfit product does not sell clothes".
- The exclusion affects review/compliance material, page copy, interface fields, data model, or acceptance criteria.
- The exclusion prevents a known cross-project copy error.

Flag as P1/P2:

- `P1`: boilerplate or out-of-scope text hides missing executable requirements, acceptance criteria, payment/legal rules, or handoff assets.
- `P2`: wording is verbose but the required executable requirements are still present.
- `P2`: keep-only boundary should be moved from PRD body into a compact "边界说明" note or acceptance criteria.

## HTML Visible Copy Checks

Inspect the actual HTML source and, when practical, rendered screenshots. Do not review only PRD text.

Flag visible HTML copy when it exposes internal requirement language instead of user-facing product language:

- PRD verbs: `必须`, `不展示`, `对应 HTML`, `规则`, `本期`, `验收`, `审核材料`, `需求`.
- Internal mechanism terms in ordinary UI: `模板`, `循环`, `聚合缓存`, `本地兜底`, `来源字段`, `运营策略`, `低维护`.
- Product-manager labels: `固定四档价格`, `两项核心差异`, `只放短笔记`, `不在信息流中主动打断阅读`.
- Scope-denial copy on user pages, unless placed in FAQ, agreement, payment disclosure, or review material and phrased for users.

Acceptable exceptions:

- Agreement pages may include legal/service boundary text, but should still avoid unnecessary implementation terms such as `本地缓存兜底` when a plain user-facing phrase is enough.
- FAQ may state real service limits, such as "不销售服装" or "不提供同款购买链接", when users are likely to ask.
- Review-material pages may explain service boundary, but should not copy PRD wording verbatim if it reads like internal notes.

Flag as P1/P2:

- `P1`: visible page text tells the user internal implementation or PM requirements instead of product meaning.
- `P1`: HTML copy contradicts PRD, price list, agreement, or payment facts.
- `P2`: wording is understandable but still sounds like PRD notes and should be rewritten before sharing broadly.

## Paid H5 Common Checks

Required modules unless explicitly scoped out:

- Login/onboarding with user agreement and privacy policy.
- Home/list/detail or product-specific main function.
- Membership center with package cards and benefit comparison.
- Order confirmation page/state.
- WeChat payment/signing launch simulation.
- Payment/signing return confirmation dialog.
- Payment/signing result page.
- Mine/account page.
- My orders page.
- My subscriptions page.
- Cancel auto-renewal entry/state.
- Customer service page.
- FAQ.
- User agreement.
- Privacy policy.
- Membership service agreement.
- Auto-renewal agreement for recurring packages.
- ICP filing info when applicable.
- Product-specific entries such as recycle bin, upload records, storage management, or content archive when source requires them.

Consistency checks:

- Same package names, prices, cycles, benefits, billing type, merchant short name, and service period across all surfaces.
- Payment/order pages must use the WeChat Pay merchant account's merchant short name (`商户简称`) for the user-facing merchant display. Enterprise legal name/service subject is not a substitute unless confirmed as the actual merchant short name.
- Recurring packages include auto-renewal agreement.
- One-time packages do not show auto-renewal agreement.
- Price cycles use `/30天` or `每30天`; do not use natural-month wording unless user confirms.
- Package click flow opens the exact selected package order confirmation.
- Both "payment completed" and "payment failed/problem" choices after WeChat return route to result page.
- Mine page contains orders, subscriptions, all agreements, cancel auto-renewal, customer service, FAQ.
- Agreement pages are simple reading pages, not marketing pages.

## Self-Operated Paid H5 Checks

Never infer the legal subject when creating or rewriting materials. In audit mode, list the current source value as a reminder and ask only if it is missing, conflicting, or required before a fix/sync.

After subject confirmation:

- Resolve the current confirmed phone-only customer-service route from the private source.
- Do not add a default email.
- Shared agreements can be reused with project variables replaced.
- Resolve the current package skeleton from the private source. Confirm the number of tiers, recurring-vs-one-time roles, prices, cycle, and renewal behavior instead of using public-export placeholders.
- The one-time product must not include auto-renew copy or auto-renew agreement.
- Review/application material module should cover price list, product intro, process flow, screenshots, agreements, and download/preview/version behavior.
- Agreement pages embedded in the main HTML count as present for product/prototype audit if they are readable and reachable from the expected flows. Separate agreement files are required only when the formal submission package or user asks for standalone files.
- Screenshots are required only when auditing formal payment/review materials or Feishu archive evidence. Do not list generic "key screenshots" as missing for a local product audit unless the review package is in scope.

Flag as P0/P1:

- Missing confirmed legal subject in PRD/agreement/payment materials.
- Any extra unconfirmed price or swapped recurring/one-time role.
- Any confirmed one-time tier treated as recurring, or any confirmed recurring tier treated as one-time.
- Email copied from old project without current confirmation.
- Stale product names or subjects in agreements.
- Product price list, product intro, PRD, and H5 disagree.
- Payment page uses enterprise legal name as merchant display without a confirmed merchant short name.

## Partner / Non-Self-Operated Paid H5 Checks

Ask for:

- Company/operator legal name.
- WeChat Pay merchant account merchant short name shown on the payment page.
- Customer-service phone.
- Online customer-service URL or enterprise WeChat only if partner provides it.
- Contact/registered address if legal text or review forms require it.
- Email only if partner materials, current source, user, or review form requires it.
- Whether shared self-operated agreement templates may be reused, or partner provides own legal text.

Flag as issue:

- Using self-operated phone, subject, agreement text, or merchant shorthand without confirmation.
- Mixing another branded album/project's visual assets, subject, merchant display, customer service, or legal copy.
- Using enterprise legal name/service subject where the payment page requires merchant short name.

## Refund H5 Checks

Required merchant facts:

- Project/brand name.
- Merchant short name.
- Enterprise legal name.
- Customer-service phone.
- Online service route, if any.
- Order display field: UI should say WeChat payment order number where applicable.
- Active-claim auxiliary rights rule.

Required refund rule:

- Main rights are assumed issued and are not the deciding refund check.
- Only actively claimed auxiliary rights block refund.
- If auxiliary rights were claimed, route to cannot-refund status, but do not expose the specific reason on the user-facing page.

Page semantics:

- P01 order query: refund application context.
- P02 refundable order: refund application context with amount, masked order, merchant, original-route return, 2-hour arrival.
- P03 identity verification.
- P04 second confirmation: centered modal, original-route return and 2-hour arrival visible.
- P05 submitted/success result may use refund result title and must emphasize 2-hour arrival, original route, original payment account.
- P06 cannot refund: refund application context, main title cannot process refund; no specific reason.
- P07 order not found: order query context, main title order not found; no specific reason.

Forbidden in user-facing refund HTML:

- raw `trans_id`
- parameter/API/backend/debug/PRD wording
- specific failure reason
- refund voucher invented concepts
- full order number or full phone number

## Platform/Admin/Handoff Checks

- If a tool is explicitly inside a platform, keep it in the platform archive rather than a separate project row.
- If the delivery is deployable code, do not call it a static HTML prototype.
- Code package, deployment docs, seed data, API/runtime notes, and README are first-class.
- If source docs mention one package name but the actual latest attached zip has another name, flag the mismatch.
- Do not treat admin platform requirements as user-facing H5 requirements.

## Finding Severity

- `P0`: wrong legal/payment/refund fact, wrong project merge/split, missing source, wrong package price/billing role, user-facing false statement.
- `P1`: required module missing, agreement mismatch, customer-service/merchant inconsistency, review material missing when required, Feishu permission/navigation issue.
- `P2`: weak wording, incomplete evidence, screenshot quality issue, non-blocking handoff gap.

Always include evidence and the exact question needed to unblock.

## Fix Brief Output

The user usually wants the audit result to be copied to another AI or developer who will fix the project. Convert findings into instructions for that fixer.

Required tone:

- Direct imperative: `请修改`, `请补齐`, `请保留`, `不要改`.
- No self-reporting: avoid `我检查到`, `我建议你`, `给你汇报`.
- No vague issue-only bullets. Every bullet must say what to change.

Required sections:

- `请修正以下问题`
- `必须修正`
- `需要补齐`
- `保持不变`
- `待业务确认` only when the fixer cannot infer the fact safely
- `验收标准`

Each fix item should include:

- target file or document section;
- current wrong behavior/content;
- replacement requirement or target state;
- source evidence when useful;
- constraint about what must not be changed.

When a fact is already present and likely correct, such as service subject or customer-service phone, list it under `保持不变` or `当前口径提醒`, not as a blocking question.
