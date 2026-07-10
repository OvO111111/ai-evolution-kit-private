param(
    [string]$RepoPath = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path,
    [string]$CodexHome = (Join-Path $env:USERPROFILE ".codex")
)

$ErrorActionPreference = "Stop"

function Invoke-Git {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$Args)
    & git -C $RepoPath @Args
    if ($LASTEXITCODE -ne 0) {
        throw "git $($Args -join ' ') failed with exit code $LASTEXITCODE"
    }
}

function Test-GitAncestor {
    param([string]$Ancestor, [string]$Descendant)
    & git -C $RepoPath merge-base --is-ancestor $Ancestor $Descendant
    return $LASTEXITCODE -eq 0
}

function Install-EvolutionKit {
    $skillsSource = Join-Path $RepoPath "skills"
    $memoriesSource = Join-Path $RepoPath "memories"
    $agentsSource = Join-Path $RepoPath "AGENTS.md"
    $skillsTarget = Join-Path $CodexHome "skills"
    $memoriesTarget = Join-Path $CodexHome "memories\evolution-kit-private"
    $agentsTarget = Join-Path $CodexHome "AGENTS.md"

    if (-not (Test-Path -LiteralPath $agentsSource)) {
        throw "Missing AGENTS.md in $RepoPath"
    }
    if (-not (Test-Path -LiteralPath $skillsSource)) {
        throw "Missing skills directory in $RepoPath"
    }
    if (-not (Test-Path -LiteralPath $memoriesSource)) {
        throw "Missing memories directory in $RepoPath"
    }

    New-Item -ItemType Directory -Path $skillsTarget -Force | Out-Null
    New-Item -ItemType Directory -Path $memoriesTarget -Force | Out-Null

    Copy-Item -LiteralPath $agentsSource -Destination $agentsTarget -Force
    $curatedProjectionSkills = @(
        "app-factory-h5-admin",
        "project-prd-h5-audit",
        "refund-h5",
        "metabase-bi-semantic-layer",
        "wechat-work-context"
    )
    $preservedPrivateSkills = @()
    foreach ($skillSource in Get-ChildItem -LiteralPath $skillsSource -Directory) {
        $skillTarget = Join-Path $skillsTarget $skillSource.Name
        if ($skillSource.Name -in $curatedProjectionSkills -and (Test-Path -LiteralPath $skillTarget)) {
            $preservedPrivateSkills += $skillSource.Name
            continue
        }
        Copy-Item -LiteralPath $skillSource.FullName -Destination $skillsTarget -Recurse -Force
    }
    if ($preservedPrivateSkills.Count -gt 0) {
        Write-Output "Preserved existing private-context skills: $($preservedPrivateSkills -join ', ')"
    }

    $resolvedCodexHome = (Resolve-Path -LiteralPath $CodexHome).Path
    $resolvedMemoriesTarget = (Resolve-Path -LiteralPath $memoriesTarget).Path
    if (-not $resolvedMemoriesTarget.StartsWith($resolvedCodexHome, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to clear unexpected memories target: $resolvedMemoriesTarget"
    }

    Get-ChildItem -LiteralPath $memoriesTarget -Force | Remove-Item -Recurse -Force
    Copy-Item -Path (Join-Path $memoriesSource "*") -Destination $memoriesTarget -Recurse -Force
}

if (-not (Test-Path -LiteralPath (Join-Path $RepoPath ".git"))) {
    throw "Repo not found or not a git checkout: $RepoPath"
}

Invoke-Git fetch origin main

$local = (& git -C $RepoPath rev-parse HEAD).Trim()
$remote = (& git -C $RepoPath rev-parse origin/main).Trim()

if ($local -eq $remote) {
    Install-EvolutionKit
    Write-Output "Already current at $local. Installed Codex evolution kit locally."
    exit 0
}

if (Test-GitAncestor "HEAD" "origin/main") {
    Invoke-Git pull --ff-only origin main
    Install-EvolutionKit
    $newHead = (& git -C $RepoPath rev-parse HEAD).Trim()
    Write-Output "Downloaded newer GitHub version and installed it locally: $newHead"
    exit 0
}

if (Test-GitAncestor "origin/main" "HEAD") {
    $dirty = (& git -C $RepoPath status --porcelain)
    if ($dirty) {
        Install-EvolutionKit
        Write-Output "Local repo is ahead of GitHub, but the worktree has uncommitted changes. Ask the user whether to commit/push."
        exit 2
    }

    Invoke-Git push origin main
    Install-EvolutionKit
    Write-Output "Uploaded newer local version to GitHub and installed it locally: $local"
    exit 0
}

Install-EvolutionKit
Write-Output "Local and GitHub histories diverged. Ask the user whether to merge, rebase, or choose one side."
exit 3
