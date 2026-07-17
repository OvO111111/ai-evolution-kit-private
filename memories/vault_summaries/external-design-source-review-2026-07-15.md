# External Design Source Review - 2026-07-15

## Scope

Review only the active external design/runtime sources that affect normal Codex
work. Do not import whole repositories or turn every upstream component into an
active skill.

## Decisions

- `design-taste-frontend`: reviewed `Leonxlnx/taste-skill` at `main`
  `b17742737e796305d829b3ad39eda3add0d79060`. The retained full guide has the
  same SHA256 as upstream. Keep the compressed local router and the full guide as
  an on-demand reference; do not activate its experimental sibling skills.
- `open-design-design-systems`: reviewed `nexu-io/open-design` tag
  `open-design-v0.15.0` at `79e257d62c0e6a8d9084f2a6464f08a251a5c0bb`.
  The 16 selected local design-system references match the upstream files at
  98.3% to 99.9%. Adopted only the new OpenAI usage guardrails. Rejected the
  desktop app, cloud model layer, plugin catalog, media templates, and thousands
  of unrelated design systems because they duplicate Codex capabilities or add
  context and maintenance cost without benchmark evidence.
- `agent-reach`: its WeChat reader remains pinned to
  `bzd6661/wechat-article-for-ai` `master`
  `69de9e413cca3fe6b770c40a4dec204afd5b2b3c`, which matched current upstream
  HEAD during review.
- `huashu-design`: retained reviewed baseline `v2.0`; no newer tag was found.

## Verification

- Three version-parser cases passed, including rejection of
  `pr-3706-verification-assets` as a release tag.
- External checker reported four tracked sources and no missing metadata or
  unreviewed baselines after the review.
- Owner-aware validation remained 57/57 after adding upstream metadata.

## Update Policy

All four sources are review-only or pinned-runtime. A newer revision is a
candidate, not an automatic replacement. Re-run the matching artifact or live
runtime test before changing the local default.
