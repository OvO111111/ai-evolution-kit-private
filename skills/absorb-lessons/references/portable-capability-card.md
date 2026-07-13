# Portable Capability Card Template

Use this template when an adopted evolution item gives an AI a reusable capability.
The card belongs in `AI_OPERATING_PLAYBOOK.md` or a linked focused playbook.

## Capability

One sentence naming the user outcome, not the implementation.

## Trigger

- Natural user wording, URLs, artifact types, or task conditions that select it.
- Explicit non-triggers and scope boundaries.

## Required Outcome

- What the user must receive.
- Observable checks that distinguish success from a shell, partial result, or
  installed-but-unused tool.

## Route Ladder

1. Lowest capable route.
2. More capable fallback after a proven failure.
3. Site/domain-specific or deterministic fallback.
4. Minimal user-assisted path only when supported routes are exhausted.

Name preferred tools as examples and explain the equivalent capability so another
AI runtime is not bound to one package or command.

## Failure Semantics

- State whether failure is request-, action-, route-, session-, account-, or
  domain-scoped.
- State what evidence permits escalation.
- State what must never be inferred from one failure.

## Reporting Contract

- How to report success.
- How to report partial, blocked, degraded, or unverified status.
- What evidence must be included.

## Validation

- Natural blind request.
- Expected decisions and observable outcome.
- Actual result, date, runtime, and residual limitation.
