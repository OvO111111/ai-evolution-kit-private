# Paid H5 Subscription Package

Use this reference when a company H5 product includes membership, WeChat Pay, delegated deduction, recurring payment, one-time paid products, review/application materials, or separate price-list/product-introduction/process-flow artifacts.

## Source Of Truth Rules

- Inspect current project HTML, PRD, screenshots, merchant notes, and user-confirmed facts before writing. Do not reuse old prices, merchant data, customer-service numbers, company names, AppIDs, or legal text, except for the self-operated customer-service and agreement-template defaults below.
- Treat each branded version as independent. Reuse function modules, but keep brand name, company subject, customer service, merchant display name, legal copy, visual style, and review artifacts separate.
- If a source file or handover document conflicts with current user-confirmed facts, use current confirmed facts and flag the old source as stale.

## Canonical Standard Reference For Self-Operated Paid H5

Use this section when the project is a self-operated paid H5 under the company/app-factory pattern, or when the user says the new H5 should follow the standard paid H5 pattern.

Canonical private reference page:

- Current official project document: `<CURRENT_OFFICIAL_PROJECT_DOC>`
- Current useful section: `八、会员商品与支付` / `8.1 商品清单`
- Verified extracted package facts from that page:

| Standard role | Billing type | Standard price | Cycle / renewal | Notes |
|---|---|---:|---|---|
| Top recurring tier | recurring | `<TOP_RECURRING_PRICE>` | Confirm the current cycle and renewal rule | Adapt the tier name and benefits to the current product. |
| Middle recurring tier | recurring | `<MIDDLE_RECURRING_PRICE>` | Confirm the current cycle and renewal rule | Adapt the tier name and benefits to the current product. |
| Entry recurring tier | recurring | `<ENTRY_RECURRING_PRICE>` | Confirm the current cycle and renewal rule | Adapt the tier name and benefits to the current product. |
| One-time top tier | one_time | `<ONE_TIME_PRICE>` | Confirm the current validity period; no automatic renewal | Do not show an auto-renewal agreement for this product. |

Execution rules:

- When Feishu access is available, fetch the reference page before writing and cite the fetched source in the working notes or final handoff. Do not rely only on memory or this distilled table if the live page is reachable.
- If the private source is unavailable, keep package values unresolved and explicitly state that the current source was not verified. Do not use public-export placeholders as business defaults.
- The standard package skeleton controls price, billing type, cycle, renewal behavior, and recurring-vs-one-time agreement set. It does not control product name, benefit text, company/operator subject, merchant display name, visual style, or product-specific feature scope.
- Before writing H5, PRD, agreements, price-list images, product introductions, process-flow diagrams, or Feishu archives, produce a compact package fact lock table with columns: plan name, standard role, billing type, price, cycle, benefits, agreement set, source of truth.
- If current project source, user-confirmed facts, and the standard reference disagree on price or billing type, stop and ask. Do not silently choose one, invent an extra tier, or swap recurring and one-time roles.

## Self-Operated H5 Customer-Service And Agreement Defaults

For self-operated company H5 projects under this app-factory workflow, the company/operator legal subject is never a default. Ask the user to confirm the subject for every project before writing PRD, H5, agreement text, payment material, review material, or Feishu sync content.

Default self-operated values after the subject is confirmed:

- Complaint/customer-service phone: `<CONFIRMED_SERVICE_PHONE>`
- Complaint/customer-service email: no default. Omit email from self-operated H5 agreements, privacy policy, PRD, payment materials, and review materials unless the current source or user explicitly provides an email.
- Agreement set:
  - 用户服务协议
  - 隐私政策
  - 会员服务协议
  - 自动续费服务协议

Agreement reuse rules for self-operated H5:

- Reuse the shared agreement clause set for all self-operated H5 projects.
- Replace project-specific display variables such as confirmed company/operator subject, product name, service name, membership product names, prices, service cycle, benefits, cancellation path, and page entry names.
- Do not keep stale product names such as 声之境, 每周穿搭, 云栖相册, or other project names when adapting the shared agreements.
- Do not infer the company subject from template sources, folder names, previous projects, merchant shorthand, or old review materials.
- Do not change the confirmed complaint/customer-service phone unless the current source or user explicitly overrides it.
- Do not ask the user for a complaint/customer-service email in self-operated H5 intake when the current private standard is phone-only.
- Canonical current template sources are private and must be resolved from the matching company workspace as `<PRIVATE_AGREEMENT_TEMPLATE_ROOT>`.
- Template files may contain old legal subjects. Treat them as template content only, not defaults. Replace them with the user-confirmed subject for the current project.
- Old project files may contain historical support emails. Treat them as project-specific facts, not defaults, and do not copy them unless the current source or user confirms them.

For non-self-operated or externally branded H5 projects, stop and ask for:

- Company/operator legal name.
- Merchant display name shown on the payment page.
- Complaint/customer-service phone and any online customer-service URL.
- Registered address or contact address if it must appear in legal text.
- Email address only if the partner materials, current source, user, or review form explicitly requires one.
- Whether the four agreement templates can be reused with the external entity or must be provided by the partner.

## Project-Specific Fact Discipline

- Company/operator legal subject is always a project-specific confirmed fact, including self-operated H5. Do not infer it from templates, historical projects, merchant shorthand, or local folder names.
- Email is not a required project fact by default, including self-operated H5. Do not ask for, invent, or copy an email unless the current source or user explicitly provides it.
- For self-operated app-factory paid H5, the canonical four-plan package skeleton above is reusable as the standard package model unless the current project source or user-confirmed facts explicitly override it. Still lock project-specific plan names and benefits from current sources.
- Do not infer product-price mapping from a loose price list alone. If a project has multiple prices across recurring subscription, one-time purchase, trial, discount, or display-price variants, inspect the current PRD/HTML/source package and the canonical standard reference first. If the mapping is still not explicit, ask the user before writing PRD, HTML, review material, Feishu docs, or handoff files.
- Do not store one-off project-specific price facts in this reusable reference unless they are backed by a stable source path and a validation case. Keep one-off project facts in the project archive or source package instead.

## Shared Package Data Contract

All self-operated paid H5 products should use one shared package data shape across the membership page, order confirmation, payment result, my orders, my subscriptions, agreement text, price list, product introduction, and PRD. Do not let each page invent its own package fields or price copy.

Minimum package fields:

```ts
type MembershipPlan = {
  planId: string
  planName: string
  billingType: "recurring" | "one_time"
  price: number
  currency: "CNY"
  cycleDays: number
  benefits: string[]
  limits?: Record<string, string | number>
  isRecommended?: boolean
  merchantDisplayName: string
  agreementSet: Array<"user_agreement" | "privacy_policy" | "membership_agreement" | "auto_renew_agreement">
}
```

Rules:

- `billingType` is mandatory. Do not infer recurring vs one-time only from product name.
- The membership page, order confirmation, my orders, my subscriptions, agreements, price-list poster, product-introduction poster, and PRD must use the same package names, prices, cycles, benefit names, and merchant display name.
- Recurring packages include the auto-renew agreement; one-time packages do not.
- Package comparison should compare only confirmed project benefits and limits. Do not add features such as favorites, likes, AI generation, invoice, refund, or customer-service channels unless current source or user confirms them.

## Paid H5 Page Contract

Paid/subscription H5 prototypes and PRDs must cover the full user loop unless the current project explicitly scopes a page out and the omission is recorded in assumptions and acceptance criteria.

### Membership Page

- Show package cards, recurring/one-time distinction, prices, cycle, recommendation mark when applicable, and key benefits.
- Show a package comparison section when there are multiple packages or tiered benefits.
- Clicking a package opens the order confirmation page/state for that exact package.
- Package data must come from the shared package data contract, not hard-coded page copy.

### Order Confirmation Page

- Show selected package name, billing type, price, cycle, key benefits, order info, merchant display name, payment method, and agreement checkboxes.
- Continuous subscription orders must show user agreement, privacy policy, membership service agreement, and auto-renewal agreement.
- One-time purchase orders must show user agreement, privacy policy, and membership service agreement only.
- The primary action should simulate launching WeChat payment, delegated deduction, or signing according to the current project.

### Payment Or Signing Return

- After the simulated WeChat payment/signing launch, show a return confirmation dialog such as "payment completed" / "encountered a problem".
- Whether the user taps success or failure, route to the payment/signing result page. Do not leave the prototype at the order page after the return dialog.

### Payment Or Signing Result Page

- Show result state: success, failed, processing, or canceled according to current prototype scope.
- Include readable order/package summary and service-cycle information when available.
- Provide practical shortcuts such as use the main feature, view orders, view subscription, or return home.

### Mine / Account Page

- Show personal/account summary, current membership status, service validity, and key account actions.
- Required entry list: my orders, my subscriptions, user agreement, privacy policy, membership service agreement, auto-renewal agreement, cancel auto-renewal, customer service, FAQ, and ICP filing info when applicable.
- Product-specific entries may be added, such as recycle bin, storage management, upload records, or content archive, but they must not replace the required account/payment/legal entries.

### My Orders Page

- Show a list of orders; an order-detail page is optional unless explicitly requested.
- Minimum fields: package/product name, order number or payment credential, amount, payment time, service cycle, payment/refund/signing status.
- Optional actions can include refund, cancel signing, or invoice request only when the current project source or user confirms those operations.

### My Subscriptions Page

- Show current package, open date, expiration date, next deduction time, auto-renewal status, and service-cycle explanation.
- Provide renewal/continue button that opens the order confirmation page for the current package.
- Provide cancel auto-renewal entry. Cancellation copy must say it stops the next cycle charge and paid benefits remain valid until the current paid cycle ends.

### Agreement Pages

- User agreement, privacy policy, membership service agreement, and auto-renewal agreement should be plain reading pages.
- Keep layout simple: titles, paragraphs, lists, and occasional emphasis. Do not turn agreement pages into marketing or feature pages.
- Replace variables per current project: product name, company/operator subject, service name, package names, prices, cycle, benefits, cancellation path, customer-service phone, merchant display name, and page entry names.
- Do not copy stale project names, subjects, prices, emails, phone numbers, or merchant display names from template files.

### Customer Service Page

- Show customer-service/complaint contact methods from current source or user-confirmed facts.
- For self-operated H5, use the current confirmed phone-only route after subject confirmation. Do not add email by default.
- For non-self-operated H5, ask for customer-service phone and online service route before writing.

### FAQ Page

- Cover common user questions that affect delivery and support: membership opening, payment/signing failed, auto-renewal, cancel auto-renewal, order lookup, refund/after-sales path, privacy/account issues, and product-specific usage limits.
- FAQ must not promise unsupported product abilities.

## Membership And Payment Page Rules

- Keep product tiers and prices data-driven from the current project source. Do not hard-code previous project prices into a new project.
- For self-operated app-factory paid H5, resolve the canonical plan skeleton from the private current source. Confirm which tiers are recurring and which tier is one-time before implementation.
- Recommend the highest recurring tier first when the project has multiple recurring tiers. Put the one-time product last unless the user says otherwise.
- Use `/30天` and `每30天` for 30-day products. Do not use `/月`, `每月`, `单月`, or `包月` unless the user explicitly overrides this rule.
- Login/onboarding agreement entry for self-operated H5 should include 用户服务协议 and 隐私政策.
- Continuous subscription payment requires checked agreement entry points for: 用户服务协议, 隐私政策, 会员服务协议, 自动续费服务协议.
- One-time purchase payment requires checked agreement entry points for: 用户服务协议, 隐私政策, 会员服务协议. Do not show 自动续费服务协议 for one-time purchase.
- Merchant display name is payment information, not a marketing button. Keep it visually ordinary.
- Payment cancel/secondary action copy must be professional, such as `取消` or `暂不开通`. Avoid flippant copy such as `再想想`.
- Cancellation flow must state: cancellation stops the next cycle charge; paid benefits remain valid until the current paid cycle ends.

## Required H5 Surfaces

At minimum, paid/subscription H5 prototypes and PRDs should cover:

- Splash or onboarding with agreement entry points.
- Phone verification login.
- Home/list page.
- Content album/list page.
- Detail/view page.
- Upload page and upload limits.
- Membership center with product cards and benefits comparison.
- Order confirmation modal/page.
- WeChat payment/signing launch simulation.
- Payment/signing return confirmation dialog.
- Payment/signing result page.
- Mine/account page.
- My orders page.
- My subscriptions page.
- Cancel auto-renewal page/state.
- Recycle bin or equivalent paid retention feature when applicable.
- Customer service page.
- FAQ.
- User agreement.
- Privacy policy.
- Membership service agreement.
- Auto-renewal agreement for recurring products.

If the current project intentionally omits any surface, state the omission in the PRD assumptions and acceptance criteria.

## Review Material Artifacts

Paid H5 review/application packages should include separate artifacts in addition to the main H5 and PRD:

| Artifact | Purpose | Format |
|---|---|---|
| Product price list | Shows product tiers, prices, benefits, cycle, and cancellation notes | PNG plus source HTML when practical |
| Product introduction page | Explains product positioning, main functions, membership products, and service scope | PNG plus source HTML when practical |
| Process-flow diagram | Shows login, upload/view, membership opening/payment, cancellation, customer service, FAQ, user agreement, and privacy policy path | PNG plus source HTML when practical |

Name artifact files in Chinese when they are user-facing, for example `产品名产品价目表.png`, `产品名产品介绍页.png`, and `产品名流程图.png`.

## PRD Material Center Requirement

For these projects, the PRD must define a standalone module for review/application materials. Use names such as `资料展示与下载`, `审核材料中心`, or `申请材料模块`.

The module must specify:

- Artifact types: process-flow diagram, product price list, product introduction page, H5 screenshot, user agreement, privacy policy, membership service agreement, auto-renewal agreement, and any required merchant/customer-service proof.
- Upload behavior: admin/operator can upload each artifact as an image, HTML source, PDF, Markdown, or attachment according to format.
- Display behavior: PRD/admin surface shows each artifact as a card/list item with title, version, updated time, owner, status, preview thumbnail, and download action.
- Preview behavior: images display inline; HTML/PDF/Markdown open in a preview page or new browser tab.
- Download behavior: each artifact has a direct download action so the user can retrieve it from the PRD/admin surface.
- Version behavior: replacing an artifact creates a new version or records the old file metadata; do not silently overwrite without trace.
- Brand behavior: branded versions have separate artifact groups; never share review material cards across brands unless explicitly marked as common.
- Acceptance criteria: user can open the PRD/admin module, preview the flowchart/price list/product intro image, and download each artifact without searching local folders.

## Product Price List / Product Introduction Pattern

When creating standalone price-list or product-introduction images:

- Keep the layout close to the reference style requested by the user, but preserve the current brand palette and positioning.
- Do not invent new product features. Copy benefits only from current project source.
- Include recurring and one-time product distinction clearly.
- Include cancellation/renewal notes for recurring products.
- Run text scan before completion for banned price wording, stale brand names, stale customer-service numbers, and accidental new feature labels.

Use `assets/product-posters.css` as a compact starting style when generating 375px mobile poster HTML.

## Process Flow Diagram Pattern

Use an 18-step flow by default for WeChat Pay delegated-deduction H5 review diagrams unless the current project requires a different path:

1. Splash/onboarding.
2. Phone verification login.
3. Home.
4. Browse list/album.
5. Detail view.
6. Upload.
7. Membership center.
8. Order confirmation.
9. WeChat payment/signing launch.
10. Payment/signing return confirmation dialog.
11. Payment/signing result.
12. Mine/account.
13. My orders.
14. My subscriptions.
15. Cancel auto-renewal.
16. Customer service.
17. FAQ.
18. Agreements: user agreement, privacy policy, membership service agreement, and auto-renewal agreement when recurring packages exist.

If the H5 file contains more frames than this list, do not claim the product has more functions. Select the confirmed main-flow frames for the diagram and leave extra states to the PRD page list or appendix.

Use `scripts/render-h5-flowchart.js` when practical. It takes a JSON config with a source H5 file, frame indexes, text labels, theme color, and output paths.

## Verification Checklist

- Render every HTML artifact to PNG and inspect it visually.
- Confirm PNG dimensions are non-zero and match the intended canvas.
- Scan generated source for `/月`, `每月`, `单月`, `包月`, stale prices, stale brands, stale customer-service numbers, and unapproved functions such as 收藏/点赞.
- For phone-frame or 750px H5 artifacts, screenshots must capture the full intended canvas or target element. Do not upload a preview image that is visibly cropped, horizontally shifted, or missing the right edge.
- Confirm agreement checkbox sets differ correctly between recurring and one-time products.
- Confirm package names, prices, cycles, benefits, merchant display names, and service periods are consistent across membership page, order confirmation, result page, my orders, my subscriptions, agreements, price-list poster, product-introduction poster, and PRD.
- For self-operated app-factory paid H5, confirm the current standard prices and billing mapping appear correctly everywhere. Flag any extra price or recurring/one-time role swap before completion.
- Confirm package click flow reaches the exact selected package order confirmation page/state.
- Confirm the prototype includes payment/signing return confirmation dialog and routes both success and failure choices to the result page.
- Confirm mine/account page includes my orders, my subscriptions, user agreement, privacy policy, membership service agreement, auto-renewal agreement, cancel auto-renewal, customer service, FAQ, and ICP filing info when applicable.
- Confirm my orders and my subscriptions contain the minimum readable fields defined in the paid H5 page contract.
- Confirm agreement pages stay as plain reading pages and do not contain stale project names, stale subjects, stale prices, stale phones, stale emails, or stale merchant display names.
- Confirm self-operated H5 uses the current confirmed phone-only route after subject confirmation and does not add a default email.
- Confirm PRD includes the review-material module with preview and download acceptance criteria.
