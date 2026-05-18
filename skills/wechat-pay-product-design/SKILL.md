---
name: wechat-pay-product-design
description: "WeChat Pay product and operations guidance for H5 payment, JSAPI/public-account payment, Mini Program payment, APP payment, delegated deduction/扣费服务/预约扣费, H5 pure signing, merchant qualification, application materials, and operations-first rollout planning."
---

# WeChat Pay Product Design

Use this skill when the user asks about WeChat Pay product selection, H5 payment, public-account/JSAPI payment, Mini Program payment, APP payment, delegated deduction, pure signing, merchant platform applications, payment rollout plans, or Feishu-style progress reporting for WeChat Pay work.

## Core Workflow

1. Start with channel mapping, not platform jargon.
2. Separate payment capability from product/business surface.
3. Check merchant subject, app/page/channel, domain, ICP, APPID-MCHID binding, and special qualification requirements.
4. Treat delegated deduction as a separate gated product, not a feature automatically included with H5 payment.
5. For plans and reports, present business milestones first and keep engineering detail underneath as editable detail.

## Product Mapping

| User scenario | WeChat Pay product |
|---|---|
| Mobile browser webpage outside WeChat | H5支付 |
| Page opened inside WeChat / public-account web page | JSAPI支付 / 公众号支付 |
| WeChat Mini Program | 小程序支付 |
| Native mobile app | APP支付 |
| Recurring charge after user authorization | 委托代扣 / 扣费服务 / 预约扣费 |
| User signs first, payment happens later | 纯签约 + later扣费 flow |

If the user mentions “微信开放平台 H5 产品绑定”, correct it early: H5 payment is applied for in WeChat Pay Merchant Platform, not by binding an H5 product in WeChat Open Platform.

## H5 Payment Checklist

- Merchant has a WeChat Pay merchant account.
- Scenario is mobile browser H5, not WeChat in-app browser and not app WebView unless official docs say the current flow supports it.
- Merchant subject/category is eligible.
- Payment domain is publicly accessible and shows real business content.
- Payment domain has ICP filing screenshot.
- Business scene screenshots include homepage and商品/服务页 with URL, name, price, and description.
- If domain主体 differs from merchant主体, prepare relationship proof, authorization letter, domain owner qualification, and cooperation agreement as required.
- Application path: 微信支付商户平台 -> 产品中心 -> H5支付 -> 申请开通.

## Delegated Deduction Checklist

- Confirm whether merchant already has delegated deduction/扣费服务 permission.
- If not, expect operations/gray-release evaluation rather than a purely self-serve switch.
- Determine merchant access mode; current docs for预约扣费 mention ordinary direct mode and ordinary service-provider mode.
- Apply delegated deduction template before interface development.
- Template must pass review before接口开发/预约扣费 use.
- H5 pure signing needs signing-origin domain permission; domain comes from request `referer`.
- App pure signing may require OpenBusinessWebview permission.
- If H5 signing must return to an app, check return-to-app permission and URL-Scheme/UA/AppID requirements.

## Product Design Outputs

When asked to design a payment product, produce:

- Channel decision table.
- User journey: open page -> confirm order/signing -> WeChat confirmation -> success/failure/return -> merchant result page.
- Merchant application checklist.
- Risk/approval checklist.
- Data fields and state machine: not applied, submitted, approved, rejected, configured, testing, live.
- Edge cases: rejected permission, domain mismatch, ICP mismatch, template not approved, user cancels, return URL failure, signing succeeds but later扣费 fails.

## Operations Planning Pattern

For this user, prefer an operations-first view:

- Top: one-screen four-week matrix or milestone summary.
- Bottom: editable detail table/Base/Gantt.
- Highlight business milestones: 注册商户号, 申请H5支付, 申请委托代扣, 申请纯签约, 模板/域名权限, 验收上线.
- Merge low-value engineering detail like internal联调 unless it materially affects approval or launch.

Default known context until user updates it:

- 声之境: 开发完成，委托代扣申请已提交.
- 云栖相册: 排期中 -> 开发/测试中 -> 再提交委托代扣.

## References

- Read `references/wechat-pay-application-notes.md` for official-doc-backed payment product details.
- Read `references/operations-reporting-pattern.md` for Feishu/product-management presentation rules.
