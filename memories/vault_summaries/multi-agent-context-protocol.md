---
page_type: decision
created_at: "2026-05-18"
updated_at: "2026-05-18"
sensitivity: personal
source_ids: ["memory_registry", "self_evolution_ledger"]
confidence: high
status: active
---

# Multi-Agent Context Protocol

## Problem

The user rejected fake multi-agent work where agents receive broad context, duplicate work, and fill the main context without clear isolation.

## Decision

Use multi-agent work only when there are independent subtasks. The main agent owns integration and final judgment.

## Protocol

- Share only the minimum task packet.
- Separate sensitive and non-sensitive context.
- Do not broadcast raw private material unless required.
- Require evidence-bearing outputs with paths, commands, sources, or changed files.
- Keep one integration owner.
- Use agents for parallel, bounded, non-blocking tasks.
- Do not outsource the immediate critical-path blocker.

## Output Standard

Every sub-agent result should state:

- what it inspected
- what it changed or found
- evidence
- uncertainty or skipped checks
- next action if integration is needed
