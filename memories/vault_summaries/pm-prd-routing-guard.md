---
page_type: decision
created_at: "2026-05-19"
updated_at: "2026-05-19"
sensitivity: personal
source_ids: ["pm_prd_routing_failure"]
confidence: high
status: active
---

# PM PRD Routing Guard

## Decision

PRD, solution plan, product requirements, backend/admin prototype, grey-release decision system, complaint workflow, and "方案 + HTML/mockup" tasks must trigger `pm-prd` before drafting.

## Required First Step

Build a context packet from real sources:

- existing PRD files
- mockup HTML
- screenshots
- customer/complaint samples
- interface/API docs
- existing workflow
- confirmed business boundaries
- user-provided acceptance constraints

## Failure Pattern To Avoid

Do not output generic PRD text, flowcharts, industry wording, or imagined project style before locating and reading the real reference material.

Installed skills are only coverage. They do not improve output unless the agent actually routes through the skill workflow and follows it.

## Success Standard

Before writing the artifact, the assistant should be able to state:

- what sources were read
- what current-state facts were extracted
- what target decision the document should support
- what is out of scope
- what acceptance criteria make the result reviewable
