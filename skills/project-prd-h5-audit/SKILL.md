---
name: project-prd-h5-audit
description: "Audit company/work project PRDs, H5 HTML prototypes, Feishu archives, and handoff packages for rule compliance. Use when the user asks to 检查项目, 审计上传的项目, 检查飞书项目, 检查 PRD/HTML/H5 是否符合 H5 skill/refund skill/自营产品/合作方产品要求, or wants to find missing membership, payment, refund, agreement, merchant, legal subject, customer service, review-material, screenshot, or development-package issues before sync, release, or handoff. This skill reports problems and questions; it does not generate the product or sync Feishu by itself."
---

# Project PRD/H5 Audit

Use this skill to find problems in existing project materials. The goal is to catch wrong assumptions, stale cross-project copy, missing modules, and incomplete handoff material before the project is treated as ready.

This is an audit skill, not a generation or sync skill. Do not edit local PRD/HTML/source packages, and do not write Feishu unless the user separately asks to sync or fix an archive.

## Required Workflow

1. **Lock the source set**
   - If the user gives Feishu docs, fetch the current Feishu content first.
   - If the user names a project but does not give a Feishu URL, first search the official Feishu navigation/current uploaded docs, then search local sources such as Codex, WorkBuddy, Desktop project folders, Downloads, PRD/HTML/output folders, and package folders.
   - If Feishu has no matching archive, continue with local PRD, HTML, screenshots, package, and support files. Do not treat "not uploaded to Feishu" as an audit failure unless the user explicitly asks to check sync/archive state.
   - If auditing all uploaded projects, fetch only official project rows from the Feishu navigation/index. Do not include process candidates or unfinished experiments as official projects.
   - Produce a source map before judging: project name, doc URL/path, PRD, HTML, screenshots, package, support files, missing sources.

2. **Classify each project**
   - `refund_h5`: refund application/query H5.
   - `paid_self_operated_h5`: company self-operated paid/member/subscription H5.
   - `paid_partner_h5`: paid/member/subscription H5 for an external partner or independently branded entity.
   - `platform_or_admin`: admin/backend/internal tool/platform.
   - `handoff_package`: code/dev package delivery where PRD + HTML is not enough.
   - If the type is unclear, ask before applying the wrong checklist.

3. **Run the audit matrix**
   - Read `references/checklists.md`.
   - Use `scripts/audit_project_text.cjs` for a first-pass keyword matrix when multiple docs are involved, then manually inspect flagged items.
   - For refund H5, also use `refund-h5` rules and its validator when local HTML/PRD exists.
   - For paid H5, also use `app-factory-h5-admin` paid subscription rules.
   - For Feishu archive/sync state, also use `feishu-prd-html-sync` rules.
   - Treat PRD information density as a product-quality check, not only a writing-style issue.
   - When a runnable H5 or admin exists and readiness is in scope, use `adversarial-review` black-box mode after the static/source audit. A rendered page, screenshot set, or keyword matrix is not live-flow evidence.

4. **Ask only high-impact questions**
   Ask when the answer changes payment, legal/compliance, user-facing copy, product type, merchant display, refund rule, customer service, package contents, or whether projects should be merged/split. Do not ask for routine implementation sequencing.

5. **Report findings first**
   Output must be written as a copyable fix brief for the AI/developer who owns the project, not as a conversational report to the user.
   Start with a short command-style conclusion: `请修正以下问题`.
   Then list actionable fixes by priority. Each item must include:
   - exact target file/doc/surface;
   - what is wrong;
   - how to fix it;
   - what not to change;
   - evidence path/line when available.

## Hard Rules

- Never invent or silently default the company/operator legal subject when creating, rewriting, or syncing project materials. During audit, report the subject currently written in the source as an observed fact/reminder, and only ask when it is missing, conflicting, or needed for a fix.
- The payment-page merchant display must be the WeChat Pay merchant account's merchant short name (`商户简称`). Do not substitute enterprise legal name, service subject, project name, or brand name unless the source/user confirms that exact value is the merchant account short name. If the source only shows an enterprise legal name as `merchantDisplayName`, flag it as a likely missing merchant-short-name field.
- Enterprise legal name belongs in PRD/config/legal/agreement context and should not be placed on ordinary front-stage pages unless the page is legal/payment/support material.
- For self-operated paid H5, resolve the current private standard for the phone-only customer-service route after subject confirmation. There is no public-export default email or phone number.
- Self-operated agreement templates are reusable, but variables must be replaced per project: product name, confirmed subject, merchant display name, package names, prices, cycle, benefits, customer-service phone, cancellation path, and page entry names.
- For self-operated paid H5, resolve the current private package model before audit. Preserve the confirmed recurring-vs-one-time roles and renewal behavior; public-export placeholders are not business defaults.
- Paid H5 must keep package data consistent across membership, order confirmation, payment/signing result, orders, subscriptions, agreements, price-list image, product-introduction image, PRD, and Feishu archive.
- Partner/non-self-operated products require confirmation of legal entity, merchant display name, customer-service phone/online route, address/email only when required, and whether the shared agreement templates can be reused.
- Refund H5 must include the active-claim auxiliary-right rule: only actively claimed auxiliary rights block refund; primary rights are assumed issued and are not the deciding check.
- Refund H5 P06/P07 must not expose specific failure/not-found reasons. P04 must be a centered modal. P02/P04/P05 must emphasize original-route return and 2-hour arrival.
- Review/application materials are first-class deliverables for paid H5 when required: price list, product introduction, process flow, application screenshots required by the payment/review channel, agreement pages or exported agreement files only when the channel requires separate files, and source HTML/PNG where practical. If the prototype already contains readable agreement pages, count agreements as present for product audit; do not demand separate agreement files unless doing formal submission packaging.
- Development packages are first-class handoff materials. If a project has a zip/package/API contract/runtime rules/assets/source list, do not call PRD + HTML sufficient.
- Feishu archive claims must be traceable. If a Feishu table lists screenshots, files, packages, or review materials, each item should map to a current local source path, package entry, or Feishu attachment. Flag missing or stale claimed artifacts.
- Feishu archive wrapper text must not dominate the reader's first screen. Flag top-of-document sync logs and archive scaffolding such as "同步时间", "同步结论", "归档信息", "已附截图", and "已附文件" when they appear before the actual PRD/product content. These may exist as a compact appendix or source map, but not as the main opening of a shareable PRD.
- Feishu-generated image descriptions are not authoritative. If image alt text or OCR-like description conflicts with the source PRD, HTML, or image file, flag it as a Feishu display/evidence-quality issue and verify against the source asset.
- Feishu navigation must show only official current projects. Unfinished candidates, process explorations, ambiguous HTML-only drafts, or old variants should be reported in chat or audit notes, not added as formal navigation rows.
- HTML previews inserted into Feishu must not be blank, cropped, horizontally shifted, or missing the right edge.
- A runnable H5 cannot pass a readiness audit from source text and screenshots alone. The black-box pass must avoid code inspection until findings are frozen, use a real `375px` or `390px` viewport, exercise the applicable primary, invalid-input, back, refresh, re-entry, empty, loading, and error paths, and attach reproduction evidence. Keep this audit skill read-only; return the resulting fix brief to the owning implementation workflow.
- User-facing HTML copy must not expose PRD language, requirement notes, internal operating mechanisms, implementation constraints, or audit/review wording. Flag visible text such as "fixed four prices", "core differences", "this is not shown", "only put short notes", "not interrupting the feed", "template/cycle/cache/fallback", or similar requirement prose unless it is rewritten as natural user-facing product copy or legally necessary agreement text.
- PRD text must be decision-dense. Flag boilerplate product positioning, generic user-value claims, broad "goals/principles/background" prose, and long "out of scope / this phase does not include" lists when they do not directly constrain UI, data, payment, compliance, review material, or development handoff. Keep only exclusions that prevent a likely wrong build or review rejection.

## Output Shape

Default output is a copyable fix brief. Avoid "我检查了/我建议/给你汇报" phrasing. Write directly to the fixer.

For one project:

```markdown
请修正以下问题。本项目当前来源：...

必须修正：
- P0/P1: [文件/页面] 问题 -> 修改要求。不要改...

需要补齐：
- [产物/字段] 补齐要求。

保持不变：
- 已正确的价格/协议/页面/主体/电话等，不要误改。

待业务确认：
- 只列修复方无法自己判断、且会影响支付/法律/上线的字段。
```

For multiple projects, start with a compact project/fix matrix, then provide one copyable fix brief per project. Do not bury P0/P1 issues below summaries.
