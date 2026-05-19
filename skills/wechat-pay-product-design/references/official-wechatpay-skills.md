# Official WeChat Pay Skills Boundary

Official upstream:

- GitHub: https://github.com/wechatpay-apiv3/wechatpay-skills
- Install command reported by public coverage: `npx skill s add https://github.com/wechatpay-apiv3/wechatpay-skills --yes`

The official repository currently organizes skills by WeChat Pay product:

- `wechatpay-basic-payment`
- `wechatpay-deduction-service`
- `wechatpay-medical-insurance-payment`
- `wechatpay-payscore`
- `wechatpay-product-coupon`

Official README states five capability areas:

1. Product selection inside a WeChat Pay product family.
2. Runnable code examples for end-to-end flows.
3. Knowledge Q&A for parameters, state transitions, callbacks, certificates, and errors.
4. Quality checks against launch checklists.
5. Troubleshooting from error codes, messages, and request/response payloads.

## Fusion Strategy

Do not duplicate the official skill's implementation knowledge inside this user skill. Treat official WeChat Pay Skills as the upstream implementation authority.

This local skill adds the user-specific layer:

- map the user's business scenario to payment product path
- correct old mental models such as "WeChat Open Platform H5 product binding"
- separate H5 payment from delegated deduction permissions
- produce product/operations checklists and Feishu-style progress views
- keep user-specific reporting and decision habits

## When To Use Which

Use this local skill first when the question is:

- Which product should we apply for?
- Is this H5, JSAPI, Mini Program, APP, or delegated deduction?
- What merchant/application material or approval risk matters?
- How should we plan/report the rollout?
- How should the user-facing payment/signing flow be designed?

Use official WeChat Pay Skills first when the question is:

- Give runnable Java/Go/Python integration code.
- Generate JSAPI/H5/APP/Mini Program payment API calls.
- Implement signature generation, certificate loading, callback verification, or refund handling.
- Check whether a codebase is launch-ready.
- Diagnose `SIGN_ERROR`, callback failure, certificate errors, refund errors, or request payload problems.

For mixed tasks, use both:

1. Local skill decides product path and business constraints.
2. Official skill provides API-level implementation.
3. Local skill translates result into plan, risk list, PRD, or status report.
