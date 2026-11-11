#Requires -Version 5.1
<# Offline installer. Keep this file beside the complete afta-security folder. #>
[CmdletBinding()]
param(
    [ValidateSet('all','claude-code','copilot','cursor','codex')]
    [string]$Agent = 'all',
    [ValidateSet('user','project')]
    [string]$Scope = 'user',
    [string]$Project,
    [switch]$Force,
    [switch]$DryRun
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$sourceDir = Join-Path $PSScriptRoot 'afta-security'
if (-not (Test-Path -LiteralPath (Join-Path $sourceDir 'SKILL.md') -PathType Leaf) -or
    -not (Test-Path -LiteralPath (Join-Path $sourceDir 'references/catalog.json') -PathType Leaf)) {
    throw 'Keep install.ps1 beside the complete afta-security folder.'
}
if ($Scope -eq 'project') {
    if (-not $Project) { $Project = (Get-Location).Path }
    if (-not (Test-Path -LiteralPath $Project -PathType Container)) { throw "Project does not exist: $Project" }
    $base = (Resolve-Path -LiteralPath $Project).ProviderPath
} else {
    if ($Project) { throw '-Project requires -Scope project.' }
    $base = [Environment]::GetFolderPath('UserProfile')
    if (-not $base) { $base = $HOME }
}
$sourceDir = (Resolve-Path -LiteralPath $sourceDir).ProviderPath
$sourcePrefix = $sourceDir.TrimEnd([char[]]@('/','\')) + [IO.Path]::DirectorySeparatorChar
if (($base.TrimEnd([char[]]@('/','\')) + [IO.Path]::DirectorySeparatorChar).StartsWith($sourcePrefix, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Choose a project outside the packaged skill source directory.'
}
# Shared Agent Skills path covers Codex, Copilot, Cursor; Claude needs its own.
$roots = switch ($Agent) {
    'all'         { '.agents/skills'; '.claude/skills' }
    'codex'       { '.agents/skills' }
    'claude-code' { '.claude/skills' }
    'cursor'      { '.cursor/skills' }
    'copilot'    { if ($Scope -eq 'project') { '.github/skills' } else { '.copilot/skills' } }
}
function Test-IdenticalFolder([string]$Left, [string]$Right) {
    $leftFiles = @(Get-ChildItem -LiteralPath $Left -Recurse -Force -File)
    $rightFiles = @(Get-ChildItem -LiteralPath $Right -Recurse -Force -File)
    if ($leftFiles.Count -ne $rightFiles.Count) { return $false }
    foreach ($file in $leftFiles) {
        $relative = $file.FullName.Substring($Left.Length).TrimStart([char[]]@('/','\'))
        $other = Join-Path $Right $relative
        if (-not (Test-Path -LiteralPath $other -PathType Leaf)) { return $false }
        if ((Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash -ne
            (Get-FileHash -LiteralPath $other -Algorithm SHA256).Hash) { return $false }
    }
    return $true
}
$plans = @()
foreach ($root in $roots) {
    $target = Join-Path (Join-Path $base $root) 'afta-security'
    $mode = 'install'
    if (Test-Path -LiteralPath $target) {
        $item = Get-Item -LiteralPath $target -Force
        if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw "Refusing a link target: $target" }
        if (-not $item.PSIsContainer) { throw "Destination is not a directory: $target" }
        if (Test-IdenticalFolder $sourceDir $target) { $mode = 'skip' }
        elseif ($Force) { $mode = 'update' }
        else { throw "Different install exists: $target (use -Force to back it up and update)." }
    }
    $plans += [PSCustomObject]@{ Target = $target; Mode = $mode }
}
foreach ($plan in $plans) {
    if ($plan.Mode -eq 'skip') { Write-Host "Already installed: $($plan.Target)"; continue }
    if ($DryRun) { Write-Host "Would $($plan.Mode): $($plan.Target)"; continue }
    $stage = Join-Path $base ('.afta-stage.' + [Guid]::NewGuid().ToString('N'))
    $backup = $null
    try {
        $parent = Split-Path -Parent $plan.Target
        [void][IO.Directory]::CreateDirectory($parent)
        [void][IO.Directory]::CreateDirectory($stage)
        # -Force includes hidden files; LiteralPath handles spaces and brackets.
        Get-ChildItem -LiteralPath $sourceDir -Force | ForEach-Object {
            Copy-Item -LiteralPath $_.FullName -Destination $stage -Recurse -Force
        }
        if ($plan.Mode -eq 'update') {
            $backupRoot = Join-Path $base '.afta-security-backups'
            [void][IO.Directory]::CreateDirectory($backupRoot)
            $backup = Join-Path $backupRoot ($Agent + '-' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '-' + [Guid]::NewGuid().ToString('N'))
            Move-Item -LiteralPath $plan.Target -Destination $backup
        }
        Move-Item -LiteralPath $stage -Destination $plan.Target
        Write-Host "Installed: $($plan.Target)"
        if ($backup) { Write-Host "Previous copy backed up: $backup" }
        $backup = $null
    } catch {
        if ($backup -and -not (Test-Path -LiteralPath $plan.Target)) {
            Move-Item -LiteralPath $backup -Destination $plan.Target
        }
        throw
    } finally {
        if (Test-Path -LiteralPath $stage) { Remove-Item -LiteralPath $stage -Recurse -Force }
    }
}
Write-Host 'Done. Start a new agent session in your project.'
