---
page_type: decision
created_at: "2026-05-18"
updated_at: "2026-05-18"
sensitivity: personal
source_ids: ["memory_registry", "self_evolution_ledger"]
confidence: high
status: active
---

# Export Boundaries

## Decision

Maintain two different surfaces:

- private vault: may include sensitive raw materials locally when explicitly ingested
- generic export bundle: only reusable, redacted, non-secret habits, skills, rules, and evolution decisions

## Generic Export Includes

- operating habits
- global rules
- skills and skill summaries
- self-evolution ledger
- project registry and lookup hints
- non-sensitive decision summaries
- redacted task packets

## Generic Export Excludes

- cookies, passwords, API keys, OAuth tokens
- account state
- raw work group messages
- raw Feishu/WeChat private content
- customer/payment/refund data
- large project directories
- dependency/build/cache folders

## Push Cadence

Do not push every self-evolution update immediately. Accumulate locally and push when explicitly requested, at stable batch points, or roughly weekly.
