# Public Evolution Export Projection Policy

The public evolution repository is a portable, redacted projection of local Codex behavior. It is not a byte-for-byte mirror of `%USERPROFILE%/.codex`.

## Directly Syncable

Generic skills, routers, validators, and source-independent operating guidance may be copied when they contain no private facts and pass `tools/check_export_safety.py`.

## Curated Projections

Project-derived or private-context-aware skills must be updated as reviewed projections, not recursively overwritten from local source:

- `app-factory-h5-admin`
- `project-prd-h5-audit`
- `refund-h5`
- `metabase-bi-semantic-layer`
- `wechat-work-context`
- any future skill containing company paths, current prices, contacts, legal subjects, document identifiers, account state, customer/payment data, or private project facts

Keep the reusable trigger, sequence, decision rules, and validation contract. Replace private values with explicit placeholders such as `<CURRENT_OFFICIAL_PROJECT_DOC>`, `<PRIVATE_COMPANY_H5_ROOT>`, `<CONFIRMED_SERVICE_PHONE>`, and `<CURRENT_CONFIRMED_PACKAGE_MODEL>`.

## Hard Rules

- Never run a recursive local-to-export copy over a curated projection.
- Apply reviewed behavioral diffs to both local source and the sanitized export projection separately.
- Public placeholders must never be used as business defaults; matching private sources must be re-read at execution time.
- Run `tools/check_export_safety.py` after projection updates and before staging.
- Keep project screenshots, raw browser traces, source packages, and private test data out of the public repository. Store only aggregate evidence.
- If a safe projection cannot be produced confidently, skip that skill and report the blocker.

## Verification

For every curated projection update:

1. Compare the behavioral sections with the local skill.
2. Confirm all private facts were replaced or removed.
3. Run skill validation and relevant route/behavior tests against the local source.
4. Run export safety scan against the public projection.
5. Review the staged diff before commit.
