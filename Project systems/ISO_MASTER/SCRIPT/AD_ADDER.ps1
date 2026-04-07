# Paramètres
$NomDomaine = "sXXXXXXX"
# $OU = "OU=Postes,DC=assist-evolution,DC=com"  # Tu peux commenter cette ligne si l'OU est inconnue
$NomUtilisateurAD = "sXXXXXXX"

# Demande du mot de passe de manière sécurisée (masqué)
$SecurePassword = Read-Host "Entrez le mot de passe pour $NomUtilisateurAD" -AsSecureString
$Credential = New-Object System.Management.Automation.PSCredential ($NomUtilisateurAD, $SecurePassword)

# Joindre le domaine (avec OU spécifique si connue)
Add-Computer -DomainName $NomDomaine -Credential $Credential -Restart -Force