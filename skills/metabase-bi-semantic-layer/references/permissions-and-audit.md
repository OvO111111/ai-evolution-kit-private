# Permissions And Audit Rules

Use these rules for any Metabase report that changes visibility, creates partner access, or touches permissions.

## Non-Negotiable Permission Rules

- `All Users` must not have root/default/business collection access.
- Internal users get business access through explicit internal groups, not by broad default membership.
- External partner users must belong only to `All Users` plus their partner group.
- Never infer internal identity from `is_active`, non-admin status, email existence, or ordinary account presence.
- Partner SQL must fix sensitive dimensions in the query itself; hiding filters in the UI is not enough.

## Current Guardrails

| Guardrail | Purpose | Verification |
| --- | --- | --- |
| `bi_metabase_permission_guard.sh` | Runs every 10 minutes to correct partner permission drift | Check `/var/log/bi-permission-guard.log` and daily audit |
| `codex_block_partner_forbidden_membership_trigger` | Blocks adding南宁枫桥 users to internal groups or mixing internal users into南宁枫桥 | Negative test should be blocked by DB |
| `codex_protect_nnfq_partner_card_trigger` | Blocks Web/API update/delete of card 61 except controlled scripts | Trigger must exist and be enabled |
| `metabase_daily_consistency_check.py` | Fails when permission or report config rules drift | Run after permission/report changes |

## Required Negative Tests

After partner permission changes, test:

- Partner account cannot see internal business collections.
- Partner account can run the intended report.
- Partner account cannot access source card or hidden internal card.
- Partner account cannot create a new card/query.
- Partner account cannot update/delete the controlled partner card.
- Partner account is not in `内部运营`, `Data Analysts`, or `Administrators`.

## Report Copy Rules

- If a partner report is a copy of an internal report, record the source card ID.
- Only fixed differences are allowed: fixed partner filters, hidden sensitive filters, partner collection, and partner permissions.
- Source metric formulas, titles, color groups, totals, and date formatting should sync from the source report unless explicitly approved.
- Any source report change must trigger partner-copy sync and validation.

## Change Reporting

For permission-sensitive changes, report:

- Root cause or intended change.
- Current group membership evidence.
- Collection and data permissions evidence.
- Negative test results.
- Whether hard-block triggers and guard cron are active.
- Any remaining UI affordance that is misleading but blocked server-side.
