# WeChat Pay official skill fusion

Trigger: the user asked how the local WeChat Pay skill is fused with or references the official WeChat Pay skill.

Finding:

- Local skill `wechat-pay-product-design` existed as a product/operations layer, based on prior WeChat Pay clarification memory and official merchant docs.
- The official upstream `wechatpay-apiv3/wechatpay-skills` was not installed locally and was not explicitly routed before this update.
- Official upstream covers implementation-heavy capabilities: product-family selection, runnable examples, Q&A, launch quality checks, and troubleshooting.

Applied:

- Updated `C:\Users\skzjc\.codex\skills\wechat-pay-product-design\SKILL.md` with routing rules.
- Added `references/official-wechatpay-skills.md` to keep upstream source, install pointer, boundary, and fusion strategy.

Policy:

- Do not duplicate official implementation knowledge in the local user-specific skill.
- Use the local skill for product choice, application path, qualification risk, PRD/operations planning, and reporting.
- Use official WeChat Pay Skills for API integration, signatures, certificates, callbacks, code examples, launch checklist scanning, and troubleshooting.
