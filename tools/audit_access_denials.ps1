param(
    [string]$Domain = "mp.weixin.qq.com",
    [string]$CodexHome = (Join-Path $env:USERPROFILE ".codex")
)

$ErrorActionPreference = "Stop"
$candidates = New-Object System.Collections.Generic.List[string]
$rulesRoot = Join-Path $CodexHome "rules"
if (Test-Path -LiteralPath $rulesRoot) {
    Get-ChildItem -LiteralPath $rulesRoot -Recurse -File | ForEach-Object { $candidates.Add($_.FullName) }
}
$config = Join-Path $CodexHome "config.toml"
if (Test-Path -LiteralPath $config) { $candidates.Add($config) }

$hits = @()
foreach ($path in $candidates) {
    $lineNumber = 0
    foreach ($line in Get-Content -LiteralPath $path -Encoding UTF8) {
        $lineNumber += 1
        if ($line -match [regex]::Escape($Domain) -or $line -match '(?i)decision\s*=\s*"deny"|denylist|blocklist') {
            $hits += [pscustomobject]@{ path = $path; line = $lineNumber; domain_match = ($line -match [regex]::Escape($Domain)); deny_match = ($line -match '(?i)deny|block') }
        }
    }
}

if ($hits.Count -eq 0) {
    Write-Output "NO_USER_EDITABLE_DENIAL_FOUND domain=$Domain"
} else {
    $hits | ConvertTo-Json -Depth 3
    Write-Output "USER_EDITABLE_DENIAL_CANDIDATES=$($hits.Count)"
}

Write-Output "Interpretation: a denial inside one task/tool is route-scoped unless an explicit local rule or product policy says otherwise. This audit does not alter rules and cannot override product safety policy."
