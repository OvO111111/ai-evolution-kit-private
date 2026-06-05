---
name: desktop-control
description: Legacy fallback for controlling Windows desktop apps through screenshots, window activation, mouse, keyboard, scrolling, and app launch commands. Use only when the official `computer-use` plugin is not listed in the current session, fails its lightweight connection test, or cannot cover the required non-browser GUI workflow.
---

# Desktop Control

Use this skill only as a fallback when browser/CDP, shell, Office file APIs, app-specific APIs, and the official `computer-use` plugin are insufficient or unavailable, and the task still needs visible desktop interaction.

If the official `computer-use` plugin is listed as available in the current session, read and attempt that skill first. Do not use this legacy script path merely because it is familiar.

## Tool

Run commands through:

```powershell
C:\Users\skzjc\.codex\venvs\turix-cua\Scripts\python.exe C:\Users\skzjc\.codex\skills\desktop-control\scripts\desktop.py <command>
```

Common commands:

```powershell
# Capture the full screen, then inspect the image with Codex image viewing
... desktop.py screenshot --out C:\Users\skzjc\AppData\Local\Temp\desktop.png

# List visible top-level windows
... desktop.py windows

# Activate a window by title substring
... desktop.py activate --title 微信

# Launch an app or executable
... desktop.py open --app notepad

# Mouse and keyboard
... desktop.py click --x 100 --y 200
... desktop.py doubleclick --x 100 --y 200
... desktop.py type --text "hello"
... desktop.py press --key enter
... desktop.py hotkey --keys ctrl s
... desktop.py scroll --clicks -5
```

## Workflow

1. Capture a screenshot before acting.
2. Use window titles and visible coordinates to decide the next action.
3. Prefer keyboard shortcuts when they are stable, and mouse clicks when the UI target is visually clear.
4. After each meaningful action, capture or inspect state again before continuing.
5. For Office documents, prefer file APIs (`docx`, `pptx`, `xlsx`) when editing files directly is enough; use desktop control only for UI-only workflows or user-login apps.

## Notes

- Coordinates are absolute screen pixels.
- The script uses the same Windows desktop session as the user.
- If an app is running elevated, non-elevated automation may not be able to control it.
- TuriX-CUA is also installed at `C:\Users\skzjc\.codex\tools\TuriX-CUA` for autonomous visual planning through MCP once a model API key is configured.
