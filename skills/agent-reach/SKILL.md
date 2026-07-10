---
name: agent-reach
description: Research and read public social, video, code, RSS, and difficult article sources through Agent Reach and platform-specific command paths. Use after `web-access` selects a platform-specific route, or when the user explicitly asks for Agent Reach, social-platform search, video subtitles, public WeChat-article extraction, or Agent Reach diagnostics. Do not use for ordinary pages that the built-in web or browser can read directly, and do not import cookies or perform account-changing actions by default.
---

# Agent Reach

Use the narrowest public, read-only channel that can answer the request.

## Preflight

Run `agent-reach doctor` only when the requested channel is uncertain or a previous platform command failed. Do not treat an installed command as proof that the channel works.

Prefer temporary output outside the user's project. Do not store browser cookies, tokens, passwords, or account secrets in commands, skills, logs, or exports.

## Common Read Paths

### Search

Use the built-in web search first when available. Agent Reach/Exa is a fallback for code-context or platform discovery:

```bash
mcporter call 'exa.web_search_exa(query: "query", numResults: 5)'
mcporter call 'exa.get_code_context_exa(query: "code question", tokensNum: 3000)'
```

### GitHub

```bash
gh search repos "query" --sort stars --limit 10
gh repo view owner/repo
gh search code "query" --language python
```

Use the GitHub plugin for issue, PR, CI, review, or publishing workflows.

### Video And Subtitles

```bash
yt-dlp --dump-json "URL"
yt-dlp --write-sub --write-auto-sub --sub-lang "zh-Hans,zh,en" --skip-download -o "$TEMP/%(id)s" "URL"
```

Inspect the generated subtitle file and cite the source URL. Do not bypass paid or private content.

### Public WeChat Articles

Follow the escalation ladder in `web-access`:

1. static fetch/search;
2. rendered built-in browser;
3. the user's Chrome when login state is genuinely required;
4. Agent Reach's WeChat article helper when the browser paths fail and the helper is installed;
5. extract from saved debug HTML if capture succeeds but post-processing fails.

Typical helper path:

```bash
python "$HOME/.agent-reach/tools/wechat-article-for-ai/main.py" "https://mp.weixin.qq.com/s/ARTICLE_ID"
```

Do not claim the article was read unless title/body extraction or rendered-page inspection succeeded.

### RSS And Public JSON

Use a normal HTTP client or feed parser. Preserve source URLs and publication dates.

## Failure Handling

When a channel fails, record the failure mode and move up one access layer. Do not repeat the same blocked request. Useful intermediate HTML, screenshots, subtitles, and API responses should be inspected before recapturing.

If a route requires login cookies, account authorization, posting, commenting, following, liking, publishing, or messaging, stop and use a supported logged-in browser/connector or request the exact authorization needed. Public research does not authorize account actions.

## Completion

Report which source was actually read, what access layer succeeded, and what remains unverified. Tool installation, `doctor` output, or a saved empty file is not successful source retrieval.
