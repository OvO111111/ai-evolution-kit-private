# Operations Reporting Pattern

Source basis: Codex memory from the 2026-05-15 Feishu planning/reporting rollout.

## User Preference

The user wants Feishu-native, editable reporting artifacts, not a generic software project plan. They prefer:

- business milestones over engineering task breakdowns
- dense one-screen summaries over long scrolling Gantt rows
- week-based horizontal span as the smallest meaningful reporting unit
- editable Base/detail underneath the summary

## Better Default Layout

Use:

```text
Document top: four-week matrix / operational dashboard
Document bottom: editable Base / detail table / Gantt source
```

Do not rely on Feishu Base Gantt zoom as the main reporting surface when the goal is “看全4个周”. Use a fixed matrix in the doc.

## WeChat Pay Milestone Vocabulary

Use these as business-facing rows/milestones:

- 注册商户号
- 申请 H5 支付
- 申请委托代扣
- 申请纯签约
- 申请/配置签约发起域名
- 申请/配置委托代扣模板
- 权限审核跟进
- 验收上线

Merge or hide low-value engineering tasks unless the user asks for delivery-team detail:

- internal联调
- API wiring details
- environment setup
- implementation substeps

## Current Known Project Defaults

Until the user updates them:

- 声之境: 开发完成，委托代扣申请已提交.
- 云栖相册: 排期中 -> 开发/测试中 -> 提交委托代扣申请 -> 委托代扣审核跟进.

## Four-Week Matrix Example

| 项目 | W1 | W2 | W3 | W4 |
|---|---|---|---|---|
| 声之境 | 开发完成 / 委托代扣已提交 | 权限审核跟进 | 模板/签约域名配置 | 验收上线 |
| 云栖相册 | 排期中 | 开发/测试中 | 提交委托代扣申请 | 审核跟进 |

If dates are known, replace W1-W4 with actual week labels. Keep it visible in one screen.
