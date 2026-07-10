# Efficient Lark Runbook

Use this reference before Feishu writes. The goal is to avoid slow repeated command failures.

## Preflight

1. Confirm `lark-cli` path:
   - `$env:APPDATA\npm\lark-cli.cmd`
2. Run Lark commands with a clean Lark environment. Do not let `HERMES_HOME` leak into `lark-cli`; it can route the command into the wrong Hermes-bound home/config path.

   Default PowerShell setup before Feishu writes:
   ```powershell
   $lark = Join-Path $env:APPDATA 'npm\lark-cli.cmd'
   Remove-Item Env:HERMES_HOME -ErrorAction SilentlyContinue
   & $lark auth status
   ```

   Do not restore `HERMES_HOME` inside the same Feishu execution session. If a separate Hermes task later needs it, that task should set its own environment explicitly.
3. Use `--as user` for user-owned Feishu docs unless the doc was created by the bot and bot ownership is known.
4. For docs commands, always include `--api-version v2`.

## Content Updates

Prefer file-based updates:

```powershell
& $lark docs +update --api-version v2 --doc <doc_token> --command overwrite --content '@path\to\doc.xml' --as user
& $lark docs +update --api-version v2 --doc <doc_token> --command append --doc-format markdown --content '@path\to\note.md' --as user
```

Rules:

- Use `overwrite` only before media is inserted, or when reinserting media is planned.
- Use `append` for merge notes, status corrections, and canonical-link notices.
- Use keyword fetch instead of full fetch for verification:
  ```powershell
  & $lark docs +fetch --api-version v2 --doc <doc_token> --scope keyword --keyword '项目名' --format pretty --as user
  ```

## Media

Insert both:

- preview image generated from HTML
- original HTML file as an attachment/source

Check the command result for a created `block_id` and `file_token`. If the CLI labels an HTML upload unexpectedly, do not keep retrying; verify it appears in the doc or report the limitation.

## Title Patch And JSON Quoting

PowerShell often corrupts JSON arguments for `drive files patch`. If `--params invalid format` appears once, switch immediately to a stable quoting approach such as `cmd /c` or a known-good wrapper. Do not try multiple near-identical PowerShell variants.

Known-good shape:

```powershell
cmd /c "set HERMES_HOME=& ""%APPDATA%\npm\lark-cli.cmd"" drive files patch --params ""{\""file_token\"":\""DOC_TOKEN\"",\""type\"":\""docx\""}"" --data ""{\""new_title\"":\""新标题\""}"" --as user"
```

That `cmd /c "set HERMES_HOME=& ..."` prefix means "clear HERMES_HOME for this command." It is not a Hermes route and must not point to a Hermes home.

Before using an unfamiliar lark command, inspect schema/help once:

```powershell
& $lark schema drive.files.patch --format json
& $lark docs +update --help
```

If the same command fails twice with the same error, stop and diagnose.

## Share Permissions

Default target is link-readable:

- `external_access=true`
- `link_share_entity=anyone_readable`
- UI meaning: 获得链接的人可阅读

Apply once, then verify if scope allows it. If verification requires a missing scope such as `drive:drive.metadata:readonly`, report that exact scope and do not repeat verification loops.

## Source Search

Use bounded search:

```powershell
rg --files <root> --glob '!**/node_modules/**' --glob '!**/.git/**' --glob '!**/dist/**' --glob '!**/build/**' --glob '!**/.next/**'
rg -n "项目名|旧名|页面标题|商户简称" <candidate-dir> --glob '!**/node_modules/**' --glob '!**/dist/**'
```

Avoid broad content search across all `WorkBuddy` unless a narrower folder cannot be found. If a broad search returns many candidates, summarize candidates and ask.

## Minimum Verification

For a normal sync, enough verification is:

- navigation keyword fetch for canonical project name
- navigation keyword fetch for stale old name or duplicate row
- target doc keyword fetch for canonical project name and missing-source note
- command success for media insertion
- permission apply success; permission read only if available

Do not repeatedly fetch whole documents after these checks pass.
