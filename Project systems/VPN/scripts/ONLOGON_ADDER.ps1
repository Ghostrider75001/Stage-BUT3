$taskPath = "\WireGuard\"
$taskName = "wireguard_on_demand"

$task = Get-ScheduledTask -TaskPath $taskPath -TaskName $taskName

# Ajouter un déclencheur ONLOGON
$logon = New-ScheduledTaskTrigger -AtLogOn

# Fusionner avec les triggers existants
$allTriggers = @($task.Triggers) + $logon

# Recréer avec les mêmes actions et paramètres
$actions = $task.Actions
$principal = $task.Principal
$settings  = $task.Settings

# Attention: Register-ScheduledTask accepte un ScheduledTask
# Reconstruit un objet ScheduledTask complet et vu qu'ils ont le même non, bah c'est transparrent pour nous
$new = New-ScheduledTask -Action $actions -Trigger $allTriggers -Principal $principal -Settings $settings

Register-ScheduledTask -TaskPath $taskPath -TaskName $taskName -InputObject $new -Force
Write-Host "Déclencheur ONLOGON ajouté."