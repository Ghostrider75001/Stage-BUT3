# 📦 Script PowerShell : choco_install.ps1

Ce script automatise l'installation de plusieurs applications Windows via Chocolatey.  
Il vérifie d'abord la connexion Internet, installe Chocolatey si besoin, puis installe chaque app une par une avec une notification après chaque succès.

---

## 🧱 Prérequis

- Windows avec PowerShell
- Droit d'administration
- Connexion Internet

---

## ⚙️ Fonctionnalités

- Bypass de la politique d’exécution PowerShell (`Set-ExecutionPolicy`)
- Test de la connexion Internet (ping 8.8.8.8)
- Installation automatique de Chocolatey
- Installation d'une liste d'applications
- Pop-up après chaque application installée
- Pop-up finale de confirmation

---

## 📋 Liste des applications installées

| Nom Chocolatey              | Description                 |
|----------------------------|-----------------------------|
| `googlechrome`             | Navigateur Chrome           |
| `firefox`                  | Navigateur Firefox          |
| `adobereader`              | Adobe Reader DC             |
| `python`                   | Python 3                    |
| `git`                      | Git                         |
| `vscode`                   | Visual Studio Code          |
| `winrar`                   | WinRAR                      |
| `7zip`                     | 7-Zip                       |
| `putty`                    | Client SSH                  |
| `notepadplusplus`         | Éditeur Notepad++           |
| `wireguard`               | VPN WireGuard               |
| `microsoft-office-deployment` | Installateur Office 365 |

---

## 🚀 Commande pour lancer le script

Depuis `cmd.exe` :

```cmd
powershell -ExecutionPolicy Bypass -File "C:\chemin\vers\choco_install.ps1"
```

### 🧷 Notes

Le script s’arrête automatiquement si aucune connexion Internet n’est détectée. \
Les pop-ups sont affichées à chaque étape pour faciliter le suivi visuel.