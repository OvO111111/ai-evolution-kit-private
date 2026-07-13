param(
    [string]$RepoPath = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path,
    [string]$CodexHome = (Join-Path $env:USERPROFILE ".codex"),
    [string]$WechatUrl = ""
)

$ErrorActionPreference = "Stop"
$utf8 = New-Object System.Text.UTF8Encoding($false)
[Console]::OutputEncoding = $utf8
$OutputEncoding = $utf8
$env:PYTHONIOENCODING = "utf-8"
$failures = New-Object System.Collections.Generic.List[string]

function Require-Path {
    param([string]$Label, [string]$Path)
    if (Test-Path -LiteralPath $Path) {
        Write-Output "PASS $Label"
    } else {
        $failures.Add("$Label missing: $Path")
        Write-Output "FAIL $Label"
    }
}

Require-Path "global AGENTS" (Join-Path $CodexHome "AGENTS.md")
Require-Path "web-access skill" (Join-Path $CodexHome "skills\web-access\SKILL.md")
Require-Path "agent-reach skill" (Join-Path $CodexHome "skills\agent-reach\SKILL.md")

$setup = Join-Path $CodexHome "skills\agent-reach\scripts\setup_wechat_reader.ps1"
$reader = Join-Path $CodexHome "skills\agent-reach\scripts\read_wechat_article.py"
Require-Path "WeChat reader setup" $setup
Require-Path "WeChat reader wrapper" $reader

$python = Join-Path $env:USERPROFILE ".agent-reach\venvs\wechat-article\Scripts\python.exe"
if ((Test-Path -LiteralPath $setup) -and (Test-Path -LiteralPath $reader)) {
    & $setup -CheckOnly
    if ($LASTEXITCODE -ne 0) {
        $failures.Add("WeChat reader runtime is not installed")
    } elseif (-not (Test-Path -LiteralPath $python)) {
        $failures.Add("WeChat reader Python is missing: $python")
    } else {
        $diagnose = & $python $reader --diagnose
        if ($LASTEXITCODE -ne 0 -or $diagnose -notmatch '"status": "ready"') {
            $failures.Add("WeChat reader diagnose failed")
        } else {
            Write-Output "PASS WeChat reader diagnose"
        }

        if ($WechatUrl) {
            $smokeRoot = Join-Path $env:TEMP ("codex-wechat-smoke-" + [guid]::NewGuid().ToString("N"))
            $live = & $python $reader $WechatUrl --output $smokeRoot
            if ($LASTEXITCODE -ne 0 -or $live -notmatch '"status": "ok"') {
                $failures.Add("Live WeChat body extraction failed")
                Write-Output $live
            } else {
                Write-Output "PASS Live WeChat body extraction"
                Write-Output $live
            }
        } else {
            Write-Output "SKIP Live WeChat body extraction; provide -WechatUrl to certify network behavior"
        }
    }
}

if ($failures.Count -gt 0) {
    Write-Output "PORTABILITY_CHECK_FAILED count=$($failures.Count)"
    foreach ($failure in $failures) { Write-Output "- $failure" }
    exit 1
}

Write-Output "PORTABILITY_CHECK_PASSED"
exit 0
