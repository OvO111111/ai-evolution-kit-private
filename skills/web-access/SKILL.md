---
name: web-access
description: Use when a task needs public web research, a supplied URL, a dynamic public page, login-state browser access, or selection among web, browser, platform, and repository tools. This is the access router, not a replacement for official GitHub, Chrome, in-app Browser, Playwright, or Agent Reach skills.
---

# Web Access Router

Choose the lowest capable route and escalate only after a concrete failure.

## Route Order

1. Use a connected app, structured API, local file, or repository tool when it
   already owns the source.
2. For GitHub repositories, PRs, issues, CI, reviews, or publishing, use
   `github:github` and its focused skills. Do not substitute generic web research.
3. For simple public pages and current facts, use static search/fetch first.
4. For an existing logged-in Chrome tab or browser state, use
   `chrome:control-chrome`.
5. For a dynamic public page that does not need the user's Chrome state, use
   `browser:control-in-app-browser`.
6. For a local dev server, reproducible UI flow, screenshot regression, or terminal
   browser automation, use `playwright`.
7. For public social platforms, video subtitles, difficult article sources, or a
   platform-specific route, use `agent-reach` after normal web access is insufficient.
8. Use `browser-cdp-fallback` only for a confirmed raw-CDP requirement or after the
   official browser routes fail for a technical reason.
9. Use official `computer-use` only for non-browser Windows GUI work, not as a web
   access shortcut.

## Failure Escalation

Record the actual failure before moving up a layer:

- HTTP or anti-bot response;
- missing rendered content;
- login or browser-state requirement;
- official browser policy block;
- connector unavailable;
- site-specific parsing failure.

Do not repeat the same blocked fetch method. Do not claim content was read when only
a title, guest shell, verification page, or template fallback was obtained.

Treat denials and failures as **route-scoped**, not URL- or domain-scoped. A static
fetch denial blocks that fetch method; a Chrome policy denial blocks that Chrome
action. Neither proves that the public URL is permanently unavailable. Continue
through another supported read-only route when the user's goal remains allowed.
Never invent or preserve a "permanent domain ban" from one failed attempt.

If Codex reports a persistent denial, identify its source before concluding:

- current-thread refusal or stale tool state: use a fresh task and re-run the router;
- user-editable local rule: audit it with `tools/audit_access_denials.ps1` and ask
  before removing or broadening the rule;
- product or safety policy: do not bypass it, but continue with other explicitly
  available supported tools when the policy only blocks one route.

## Login-State Boundary

Use the user's existing Chrome state only when the request requires it. Do not
export cookies, tokens, profiles, or credentials. A Chrome policy block ends that
Chrome action only. For a public article, continue with the in-app browser or the
site-specific public reader. For private content that genuinely requires the
blocked login state, report the exact limitation instead of pretending another
route read the same private content.

## URL-Based Evolution Work

When `absorb-lessons` receives a URL or repository, this router obtains the source.
`absorb-lessons` still owns overlap analysis, adoption decisions, scoping, and
validation.

## Completion Evidence

Report which access tier succeeded, what content was actually extracted, and what
could not be verified. For browser interaction, include DOM, screenshot, tool output,
or another concrete result appropriate to the task.

## Legacy CDP Reference

Open `references/legacy-cdp-guide.md` only after selecting
`browser-cdp-fallback`; it is not the default web workflow.
