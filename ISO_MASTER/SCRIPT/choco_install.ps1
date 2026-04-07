# Autorise les scripts
Set-ExecutionPolicy Bypass -Scope Process -Force

# Installe Chocolatey
Write-Host "Installing Chocolatey..."
Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
RefreshEnv

# Pause rapide
Start-Sleep -Seconds 5

# Liste des applis à installer
$packages = @(
    "wireguard",          # WireGuard VPN
    "foxitreader",        # Foxit Reader
    "python",             # Python 3
    "git",                # Git
    "office365business",  # Office 365
    "7zip",               # 7-Zip
    "googlechrome",       # Chrome
    "greenshot",          # Greenshot
    "notepadplusplus"     # Notepad++
)


# Installe les applis Chocolatey
foreach ($pkg in $packages) {
    Write-Host "Installing $pkg..."
    choco install $pkg -y --ignore-checksums
}

Write-Host "All done!" -ForegroundColor Green