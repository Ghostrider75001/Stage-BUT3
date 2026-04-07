$taskPath = "\WireGuard\wireguard_on_demand"

$service = New-Object -ComObject "Schedule.Service"
$service.Connect()

$task = $service.GetFolder("\WireGuard").GetTask("wireguard_on_demand")
$definition = $task.Definition

# Desactive l'option "Ne demarrer que si l'ordinateur est sur secteur"
$definition.Settings.DisallowStartIfOnBatteries = $false
$definition.Settings.StopIfGoingOnBatteries = $false

# Enregistre les modifications
$service.GetFolder("\WireGuard").RegisterTaskDefinition("wireguard_on_demand", $definition, 6, $null, $null, 3, $null)
