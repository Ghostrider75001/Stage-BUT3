CECI est le README DU DOSSIER Scripts DU PROJET VPN


- Auto_connect_wg.ps1 --> Script qui active le vpn sur demande en fonction du réseau sur lequel on est connecté.

- Launch_hidden.vbs --> Script à mettre dans la tâche (Wireguard_on_demand) crée dans le planificateur de tâches. il lance Auto_connect_wg.ps1 en mode silencieux

- Scheduler --> Crée une tâche (Wireguard_on_demand) dans le planificateur de taches dans le répertoire Wireguard/