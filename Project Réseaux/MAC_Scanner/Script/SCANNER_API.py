import requests
import getpass
import csv
import urllib3
import re
import os as OS
import time
from datetime import datetime

# Ignorer les avertissements SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Paramètres de connexion Aruba
controller_ip = input("Wifi controler's IP Adrr: ")
username = input("Username: ")
password = getpass.getpass("password: ")
base_url = f"https://{controller_ip}:4343"

# Création de session
session = requests.Session()
session.verify = False

# Connexion à l'API
login_url = f"{base_url}/rest/login"
login_payload = {"user": username, "passwd": password}
headers = {"Content-Type": "application/json"}
response = session.post(login_url, headers=headers, json=login_payload)

resp_json = response.json()
if resp_json.get("Status") != "Success":
    print("Échec de la connexion :", resp_json)
    exit()

sid = resp_json.get("sid")
print("Connexion établie. SID :", sid)

# Commande show clients
cmd = "show clients"
clients_url = f"{base_url}/rest/show-cmd?iap_ip_addr={controller_ip}&cmd={cmd.replace(' ', '%20')}&sid={sid}"
response_client = session.get(clients_url)
output = response_client.json().get("Command output", "")

# Récupérer la date/heure
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
csv_filename = f"clients_{timestamp}.csv"
history_file = "historique_clients.csv"

# Extraction lignes clients depuis le texte
lines = output.strip().splitlines()

# Trouver l'index de l'en-tête
for i, line in enumerate(lines):
    if line.strip().startswith("Name"):
        header_index = i
        break
else:
    print("En-tête non trouvé dans la sortie CLI.")
    exit()

# Extraire les lignes utiles
client_lines = []
for line in lines[header_index + 2:]:
    if "Number of Clients" in line:
        break
    if line.strip():
        client_lines.append(line)

# Parser chaque client
clients_data = []
for line in client_lines:
    parts = re.split(r'\s{2,}', line.strip())
    if len(parts) < 6:
        parts = [""] + parts
    name, ip, mac, os, essid, ap = parts[:6]
    clients_data.append({
        "name": name,
        "ip": ip,
        "mac": mac,
        "os": os,
        "essid": essid,
        "ap": ap,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

# Export vers CSV daté
with open(csv_filename, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["name", "ip", "mac", "os", "essid", "ap", "timestamp"])
    writer.writeheader()
    for client in clients_data:
        writer.writerow(client)

time.sleep(0.5)
print(f"Fichier généré : {csv_filename}")

# Mise à jour de l'historique
known_macs = set()
if OS.path.exists(history_file):
    with open(history_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            known_macs.add(row["mac"])

with open(history_file, "a", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["name", "ip", "mac", "os", "essid", "ap", "timestamp"])
    if OS.stat(history_file).st_size == 0:
        writer.writeheader()

    new_count = 0
    for client in clients_data:
        if client["mac"] not in known_macs:
            writer.writerow(client)
            new_count += 1

print(f"{new_count} nouveaux clients ajoutés à {history_file}")