---
aliases: [wechat, weixin, 微信, 微信公众号, 公众号, mp.weixin.qq.com]
---

# WeChat Public Articles

WeChat public articles are often readable in a real browser but blocked for static fetchers. Do not treat a Jina/curl "environment abnormal" response as proof that the article is unavailable.

## Preferred Ladder

1. Try static search/fetch once when a snippet or discovery result may be enough.
2. If the body is missing, use the official in-app Browser, or the user's Chrome
   when the existing tab/login state is genuinely required.
3. For a public article body, use the deterministic Camoufox wrapper. If the
   reader is missing, run its setup script instead of claiming the skill is ready:

```powershell
$setup = "$env:USERPROFILE\.codex\skills\agent-reach\scripts\setup_wechat_reader.ps1"
& $setup
$wechatPython = "$env:USERPROFILE\.agent-reach\venvs\wechat-article\Scripts\python.exe"
$reader = "$env:USERPROFILE\.codex\skills\agent-reach\scripts\read_wechat_article.py"
& $wechatPython $reader "<URL>"
```

4. The wrapper automatically recovers from saved debug HTML when browser capture
   succeeds but upstream post-processing fails. Manual inspection remains available at:

```text
$env:USERPROFILE\.agent-reach\tools\wechat-article-for-ai\output\debug\
```

Use BeautifulSoup selectors:

- title: `h1#activity-name`
- author: `span#js_name`
- content: `div#js_content`

Extract visible text from `p`, headings, `li`, `blockquote`, and `pre`; preserve code blocks and list order when relevant.

## Known Failure Modes

- Jina Reader commonly returns a WeChat environment verification page.
- Static `curl` commonly captures anti-bot scaffolding rather than article content.
- `wechat-article-for-ai` can succeed at browser capture but fail in its parser with `TypeError: 'NoneType' object is not callable`; the saved debug HTML is still useful.

## Safety

Do not request or store user cookies. If a browser login or verification is needed, ask the user to complete it in their own browser and continue from rendered/debug output.

A refusal from one fetcher or browser action is not a permanent ban on
`mp.weixin.qq.com`. Record the failed route, do not repeat it, and continue to the
next supported read-only route. Success requires a real title plus substantive
body text, not an environment-abnormal page.
