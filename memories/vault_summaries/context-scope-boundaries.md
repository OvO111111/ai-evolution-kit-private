---
page_type: decision
created_at: "2026-06-06"
updated_at: "2026-06-06"
sensitivity: personal
source_ids: ["user_scope_correction_2026_06_06"]
confidence: high
status: active
---

# Context Scope Boundaries

## Decision

Exported memories are not a single global instruction layer. Every memory, skill, and routing rule must be applied through a scope check.

## Scope Classes

| Scope | Applies To | Examples | Must Not Affect |
|---|---|---|---|
| Global Codex evolution | Assistant behavior that should carry across all work | outcome-first reporting, verification before completion, skill routing hygiene, memory export boundaries | project-specific product constraints |
| Personal reusable preference | User's durable working style or generally reusable standards | concise Chinese replies, pragmatic engineering judgment, source inspection before claims | company-only workflows unless matched |
| Company/work project context | Work/company projects, sources, and domain workflows | 声之境, 每周穿搭, 多应用管理平台, unified admin, WeChat work context, Feishu operations, payment rollout/customer/complaint data | personal projects, open-source projects, generic H5/admin/design work |
| Task-local fact | Current workspace or current conversation only | temporary file paths, one-off decisions, local failures | future unrelated tasks |

## Active Correction

`声之境`, `H5 app factory`, `每周穿搭`, and `unified admin` memories are company/work project context. They should be used only when the user explicitly references that project family, the workspace/source path matches it, or the user asks to reuse that company pattern.

They are not global defaults for:

- generic H5 work;
- personal projects;
- open-source projects;
- external client projects;
- unrelated PRDs;
- unrelated admin dashboards or internal tools.

## Routing Rule

Before applying any project-derived skill, ask internally:

1. Did the user name the project/company/domain/source path?
2. Is the current workspace part of that project family?
3. Did the user ask to reuse that project's pattern?

If all answers are no, the project-derived skill is out of scope. Use the normal generic skill or local project rules instead.

## Verification Prompt

When the user asks "what did you learn?" or tests sync quality, answer by separating:

- global evolution rules learned;
- company/work project memories learned;
- personal reusable preferences learned;
- what is explicitly not global.
