# WeChat Pay Application Notes

Source basis: Codex memory from the 2026-05-11 WeChat Pay clarification task plus official WeChat Pay merchant docs checked again on 2026-05-18.

## Mental Model

Do not answer WeChat Pay questions from the old “微信开放平台 H5 产品绑定” mental model. The reusable distinction:

- H5 payment is a WeChat Pay merchant-platform product permission.
- H5 payment is not a WeChat Open Platform H5 app binding.
- Delegated deduction / 扣费服务 is a separate product/permission path.

## H5 Payment

Official H5 product intro states H5 payment provides collection capability in mobile browser pages outside the WeChat client. It is not for app scenarios; app scenarios should use APP payment.

Official application path:

```text
微信支付商户平台 -> 产品中心 -> H5支付 -> 申请开通
```

Materials and checks mentioned by the official application guide:

- Payment domain.
- Payment domain ICP filing screenshot.
- Business venue / business scene description.
- Domain homepage screenshot with URL.
- 商品/服务 scene screenshot with URL, product/service name, price, and description.
- If domain主体 and merchant主体 differ, provide relationship proof / authorization letter / domain owner qualifications / cooperation agreement depending on scenario.
- Special industries may need additional licenses or authorization proof.

Official H5 product intro also gives eligibility framing:

- Supported subject types include enterprise, institution, government agency, and social organization.
- Supported app types include verified service account, verified government/media public account, verified mini program, and verified mobile app.

## Channel Selection

| Situation | Product |
|---|---|
| External mobile browser H5 page | H5支付 |
| WeChat in-app page / public-account page | JSAPI支付 / 公众号支付 |
| Mini Program | 小程序支付 |
| Native App | APP支付 |
| User authorization first, recurring/later charge | 委托代扣 / 扣费服务 |

When the user asks “是不是公众号网页这种形式”, answer directly:

- If opened inside WeChat public-account page: usually JSAPI/公众号支付.
- If opened in external mobile browser outside WeChat: H5支付.

## Delegated Deduction / 扣费服务 / 预约扣费

Official current doc checked on 2026-05-18 says 扣费服务（预约扣费） is in gray testing and not fully open. It requires preparation before access:

1. Confirm qualifications and merchant mode.
2. Apply delegated deduction template.
3. Apply signing-related permissions.

Important operational points:

- If merchant lacks delegated deduction permission, contact the aligned WeChat Pay operations contact for evaluation and application guidance.
- Current预约扣费 docs mention ordinary direct mode and ordinary service-provider mode.
- Template management is opened in the merchant platform advanced-business area with operations help.
- Template type should be 预约扣费.
- Each template corresponds to one product; standard price is the amount the product may use for预约扣费.
- Template must pass review before API development/use.
- Termination URL can be modified in merchant backend.

## H5 Pure Signing

H5 pure signing needs signing-origin domain permission. The signing-origin domain can be obtained from HTTP request header `referer`.

If the permission is missing, the user may see “商家服务异常，请联系商家处理”.

Official mail/application template fields include:

- usage background
- merchant id
- merchant subject
- template id
- signing-origin domain

Domain should be configured as full domain, for example:

- page `https://weixin.qq.com/wx/contract` -> domain `weixin.qq.com`
- page `https://qq.com/wx/contract` -> domain `qq.com`

If H5 signing must return to app, check separate return-to-app permission, `jump_control.jump_appid`, URL-Scheme, UA keyword, and target AppID.

## Product/Implementation State Machine

Use these states for product plans and dashboards:

```text
未准备 -> 商户号已注册 -> H5支付已申请 -> H5支付已开通
-> 委托代扣权限评估中 -> 模板已提交 -> 模板已通过
-> 纯签约域名权限已配置 -> 联调/验收 -> 上线
```

Keep H5 payment state separate from delegated deduction state. Do not imply H5 payment approval means deduction approval.

## Official Doc Links

- H5支付产品介绍: https://pay.wechatpay.cn/doc/v3/merchant/4012791832
- 申请H5支付权限指引: https://pay.wechatpay.cn/doc/v3/merchant/4012791841
- 各主体可申请的基础支付权限列表: https://pay.wechatpay.cn/doc/v3/merchant/4015477838
- H5纯签约: https://pay.wechatpay.cn/doc/v2/merchant/4011987295
- 扣费服务（预约扣费）接入前准备: https://pay.wechatpay.cn/doc/v3/merchant/4012161141
