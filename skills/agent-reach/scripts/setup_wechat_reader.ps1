param(
    [string]$ToolRoot = (Join-Path $env:USERPROFILE ".agent-reach\tools\wechat-article-for-ai"),
    [string]$VenvRoot = (Join-Path $env:USERPROFILE ".agent-reach\venvs\wechat-article"),
    [string]$Revision = "69de9e413cca3fe6b770c40a4dec204afd5b2b3c",
    [switch]$CheckOnly
)

$ErrorActionPreference = "Stop"
$upstream = "https://github.com/bzd6661/wechat-article-for-ai.git"
$venvPython = Join-Path $VenvRoot "Scripts\python.exe"
$mainScript = Join-Path $ToolRoot "main.py"
$lockedRequirements = Join-Path $PSScriptRoot "wechat-reader-requirements.txt"
$runtimeSmoke = Join-Path $PSScriptRoot "smoke_wechat_runtime.py"

function Test-ReaderReady {
    if (-not (Test-Path -LiteralPath $venvPython) -or -not (Test-Path -LiteralPath $mainScript)) {
        return $false
    }
    if (-not (Test-Path -LiteralPath (Join-Path $ToolRoot ".git"))) {
        return $false
    }
    $currentRevision = (& git -C $ToolRoot rev-parse HEAD 2>$null).Trim()
    if ($LASTEXITCODE -ne 0 -or $currentRevision -ne $Revision) {
        return $false
    }
    & $venvPython -c "import camoufox, markdownify, bs4, httpx" 2>$null
    if ($LASTEXITCODE -ne 0) { return $false }
    & $venvPython $runtimeSmoke 2>$null
    return $LASTEXITCODE -eq 0
}

if (Test-ReaderReady) {
    Write-Output "READY wechat-reader revision=$Revision tool=$ToolRoot venv=$VenvRoot"
    exit 0
}

if ($CheckOnly) {
    Write-Output "NOT_READY wechat-reader tool=$ToolRoot venv=$VenvRoot"
    exit 2
}

foreach ($command in @("git", "python")) {
    if (-not (Get-Command $command -ErrorAction SilentlyContinue)) {
        throw "Required command is missing: $command"
    }
}

New-Item -ItemType Directory -Path (Split-Path -Parent $ToolRoot) -Force | Out-Null
New-Item -ItemType Directory -Path (Split-Path -Parent $VenvRoot) -Force | Out-Null

if (-not (Test-Path -LiteralPath (Join-Path $ToolRoot ".git"))) {
    if (Test-Path -LiteralPath $ToolRoot) {
        throw "Tool directory exists but is not a git checkout: $ToolRoot"
    }
    & git clone $upstream $ToolRoot
    if ($LASTEXITCODE -ne 0) { throw "Failed to clone $upstream" }
} else {
    $dirty = & git -C $ToolRoot status --porcelain
    if ($dirty) { throw "Reader checkout has local changes and cannot be pinned safely: $ToolRoot" }
}

& git -C $ToolRoot fetch origin $Revision
if ($LASTEXITCODE -ne 0) { throw "Failed to fetch pinned reader revision: $Revision" }
& git -C $ToolRoot checkout --detach $Revision
if ($LASTEXITCODE -ne 0) { throw "Failed to checkout pinned reader revision: $Revision" }

if (-not (Test-Path -LiteralPath $venvPython)) {
    & python -m venv $VenvRoot
    if ($LASTEXITCODE -ne 0) { throw "Failed to create venv: $VenvRoot" }
}

& $venvPython -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) { throw "Failed to upgrade pip" }
if (-not (Test-Path -LiteralPath $lockedRequirements)) {
    throw "Missing locked dependency file: $lockedRequirements"
}
& $venvPython -m pip install -r $lockedRequirements
if ($LASTEXITCODE -ne 0) { throw "Failed to install WeChat reader dependencies" }

if (-not (Test-ReaderReady)) {
    throw "WeChat reader installation finished but dependency verification failed"
}

Write-Output "INSTALLED wechat-reader revision=$Revision tool=$ToolRoot venv=$VenvRoot"
