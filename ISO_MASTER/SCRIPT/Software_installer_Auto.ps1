# Sauvegarder et modifier la politique d'exécution
$originalPolicy = Get-ExecutionPolicy -Scope Process
Set-ExecutionPolicy Bypass -Scope Process -Force

# Vérifier si Chocolatey est installé
if (-not (Get-Command choco.exe -ErrorAction SilentlyContinue)) {
    Write-Host "Installation de Chocolatey..."
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
} else {
    Write-Host "Chocolatey est déjà installé."
}

# Forcer mise à jour de Chocolatey (optionnel mais recommandé)
choco upgrade chocolatey -y

# Liste des paquets à installer (Microsoft 365 en dernier)
$packages = @(
    "firefox",
    "googlechrome",
    "windirstat",
    "msteams",
    "vscode",
    "7zip",
    "wireguard",
    "git",
    "python",
    "adobereader",
    "putty",
    "microsoft-office-deployment"
)

# Installation des logiciels
foreach ($pkg in $packages) {
    Write-Host "`n Installation de $pkg..."
    choco install $pkg -y --no-progress
}

# Restauration de la politique d'origine
Set-ExecutionPolicy $originalPolicy -Scope Process -Force

Write-Host "`n Tous les logiciels ont été installés avec Chocolatey."