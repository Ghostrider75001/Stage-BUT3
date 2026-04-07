while ($true) {
    # Nom du WiFi auquel tu veux être connecté
    $ssidAttendu = "AssistEvolution"

    # Fonction pour avoir le nom du fichier conf
    function Get-TunnelNameFromFolder {
        $basePath = "C:\Program Files\WireGuard\Data\Configurations"

        $file = Get-ChildItem -Path $basePath -File -ErrorAction SilentlyContinue |
            Where-Object { $_.Name -like "*.conf" -or $_.Name -like "*.conf.dpapi" } |
            Select-Object -First 1

        if ($file) {
            return [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
        } else {
            return $null
        }
    }

    # Chemin vers le fichier de config WireGuard
    $basename = Get-TunnelNameFromFolder # (ex : skone.conf)
    $tunnelName2 = $basename -replace '\.conf$', '' # (ex : skone)
    $tunnelName = "C:\Program Files\WireGuard\Data\Configurations\$basename.dpapi"
    $ssidActuel = netsh wlan show interfaces |
        Where-Object { $_ -match "^\s*SSID\s*:\s*(.+)$" } |
        ForEach-Object {
            if ($_ -notmatch "BSSID") {
                ($_ -split ":\s+", 2)[1].Trim()
            }
        }

    # Fonction pour vérifier si le tunnel est actif
    function Is-VpnActive {
        try {
            $status = & 'C:\Program Files\WireGuard\wireguard.exe' /dumptunnelservice `"$tunnelName`" 2>&1
            return $status -like "*state: up*"
        } catch {
            # Write-Host "[Erreur VPN] $_"
            return $false
        }
    }

    # Logique VPN (commentaire = debug)
    try {
        if ($ssidActuel -ne $ssidAttendu) {
            if (-not (Is-VpnActive)) {
                # Write-Host "[VPN] Not connected to $ssidAttendu. VPN Activation..."
                & "C:\Program Files\WireGuard\wireguard.exe" /installtunnelservice `"$tunnelName`" 2>&1 | ForEach-Object {
                    Write-Host "[VPN] $_"
                }
            }
        } else {
            if ($ssidActuel -eq $ssidAttendu) {
                # Write-Host "[VPN] Connected to $ssidAttendu. VPN Desactivation..."
                & "C:\Program Files\WireGuard\wireguard.exe" /uninstalltunnelservice `"$tunnelName2`" 2>&1 | ForEach-Object {
                    Write-Host "[VPN] $_"
                }
            }
        }
    } catch {
        # Write-Host "[Something is BROKEN] $_"
    }
    Start-Sleep -Seconds 3
}


