# Skill update check honesty fix

## Failure

The prior weekly report said skills were checked, but the actual scope only covered official plugins, npm global tools, visible skill surfaces, and selected smoke tests. It did not check manually adapted external skills against upstream tags.

This was misleading. If the user had trusted the report, they would have believed `huashu-design` was current even though the updater had not compared it to upstream `v2.0`.

## Fix

Added `tools/check_external_skill_updates.py` to the evolution export repo.

The checker scans local skill roots for:

- `upstream`
- `upstream_ref`
- `upstream_commit`
- GitHub URLs without explicit upstream metadata

For GitHub upstreams with metadata, it runs `git ls-remote --tags --refs` and compares the latest semver-like tag with local metadata.

## Current result

Running the checker on 2026-06-09 found:

- `current=1`: `huashu-design` is now pinned to upstream `v2.0`.
- `needs_metadata=11`: `caveman-help`, `design-taste-frontend`, Open Design adapted skills, and `agent-reach` contain GitHub URLs but cannot honestly be update-checked yet because they lack upstream metadata.

## Durable rule

Future weekly update reports must separate:

1. official plugin/runtime updates checked
2. npm/global CLI updates checked
3. local skill trigger/smoke checked
4. external adapted skill upstream tags checked
5. external skills missing metadata and therefore not checked

Do not say "skills were checked for updates" unless item 4 actually ran or item 5 is explicitly reported.
