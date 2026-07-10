---
scope: global-codex-evolution
authority: superseding-correction
source: export-safety-audit
validated: 2026-07-10
---

# Export safety correction

The portable evolution export must fail closed before staging if it contains personal
absolute paths, company project roots, Feishu/Lark document or board identifiers,
private hosts, known private contacts, identity/app IDs, or secret-shaped values.

`tools/check_export_safety.py` is now required by `weekly-evolution-sync`. The final
working tree scanned 277 candidate text files with zero findings after redaction and
large optional media removal.

This does not purge previously published Git history. Removing the tracked
`memories/extensions` mirror or rewriting history is destructive and requires an
explicit user decision.

Final system regression baseline after this correction: 30 static contracts pass;
26 fresh GPT-5.6 route cases pass, with one explicitly degraded dashboard fallback.
