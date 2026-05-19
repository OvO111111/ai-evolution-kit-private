---
page_type: topic
created_at: "2026-05-18"
updated_at: "2026-05-18"
sensitivity: personal
source_ids: ["wechat_pay_rollout", "wechat_pay_product_design_skill"]
confidence: medium
status: active
---

# Payment Product Design

## Reusable Pattern

When the user asks about WeChat Pay products, map channel type to payment product type first. Then explain application path and qualification logic.

## Known Mapping

- external mobile browser webpage -> H5 payment
- WeChat in-app/public-account page -> JSAPI/public-account payment
- Mini Program -> Mini Program payment
- App -> App payment
- recurring auto-deduct after authorization -> delegated deduction / withholding service

## Reverification

Policies can drift. For current answers, re-check official WeChat Pay docs before giving final guidance.

Known doc handles to search first:

- `4012791832`
- `4012791841`
- `4015477838`
- `4011987295`
- `4012161141`

## Official Skills Fusion

Local skill `wechat-pay-product-design` is the product and operations layer. It should answer product choice, application path, qualification risk, PRD/plan, and status-reporting questions.

Official upstream `wechatpay-apiv3/wechatpay-skills` is the implementation layer. Use it for API integration, code examples, signature/certificate/callback details, launch checklist scanning, and troubleshooting.

Do not duplicate official implementation knowledge into the local skill. Keep a reference boundary and use the official repo as the authority when the task reaches code or API details.
