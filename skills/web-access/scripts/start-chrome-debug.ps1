param(
  [int]$Port = 9222,
  [string]$UserDataDir = "$env:TEMP\codex-chrome-debug-profile"
)

$chrome = Join-Path $env:ProgramFiles "Google\Chrome\Application\chrome.exe"
if (-not (Test-Path -LiteralPath $chrome)) {
  $chrome = Join-Path ${env:ProgramFiles(x86)} "Google\Chrome\Application\chrome.exe"
}
if (-not (Test-Path -LiteralPath $chrome)) {
  throw "Chrome executable not found."
}

New-Item -ItemType Directory -Force -Path $UserDataDir | Out-Null

$args = @(
  "--remote-debugging-port=$Port",
  "--user-data-dir=$UserDataDir",
  "--no-first-run",
  "--no-default-browser-check",
  "about:blank"
)

Start-Process -FilePath $chrome -ArgumentList $args
Start-Sleep -Seconds 2

$versionUrl = "http://127.0.0.1:$Port/json/version"
try {
  $response = Invoke-WebRequest -UseBasicParsing $versionUrl -TimeoutSec 5
  $response.Content
} catch {
  throw "Chrome started, but $versionUrl is not reachable: $($_.Exception.Message)"
}
