import requests
import getpass
import csv
import urllib3
import re
import time

# Skip SSL Warning (Auto signed certificates)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Manual entry of IDS
controller_ip = input("IP address of the WIFI controler: ")
username = input("Username: ")
password = getpass.getpass("Password : ")
base_url = f"https://{controller_ip}:4343"


# Étape 1 - Aruba API remote connexion
login_url = f"{base_url}/rest/login"
login_headers = {"Content-Type": "application/json"}

login_payload = {
   "user": username,
   "passwd": password
}

session = requests.Session()
session.verify = False
response = session.post(login_url, headers=login_headers, json=login_payload)

print(response)

if response.status_code != 200 :
   print("Aruba API Remote connection failed.")
   exit()


resp_json = response.json()
if resp_json.get("Status") != "Success":
   print("Login failed:", resp_json)
   exit()

sid = resp_json.get("sid")
print("Connexion established ! SID :", sid)


# Étape 2 - Get the connected clients informations
clients_url = f"{base_url}/rest/show-cmd?iap_ip_addr={controller_ip}&cmd=show%20clients&sid={sid}"
response_client = session.get(clients_url)

#print("Resultat brut : \n")
#print(response_client.text)

if response.status_code != 200:
   print("Getting connected clients FAILED : ", response_client.text)
   exit()


cli_output = response_client.json()
#print("Resultat Raffiné : \n")
#print(cli_output)

output = cli_output.get("Command output", "")

# extract only customer lines (ignore header and footer)
lines = output.strip().splitlines()

# Find the row containing the column names (reference to start the parsing)
for i, line in enumerate(lines):
    if line.strip().startswith("Name"):
        header_index = i
        break
else:
    print("Headers not found ! ")
    exit()


# Retrieve the data from the following lines ('til line "Number of Clients")
client_lines = []
for line in lines[header_index + 2:]:  # skip header + dash line (-)
    if "Number of Clients" in line:
        break
    
    if line.strip():
        client_lines.append(line)


# Export CSV
with open("clients.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "IP Address", "MAC Address", "OS", "ESSID", "Access Point"])
    for line in client_lines:
        
        # Normalize space
        parts = re.split(r'\s{2,}', line.strip())
        if len(parts) < 6:
            
            # Some names may be missing → Empty value inserted
            parts = [""] + parts
        name = parts[0]
        ip = parts[1]
        mac = parts[2]
        os = parts[3]
        essid = parts[4]
        ap = parts[5]
        writer.writerow([name, ip, mac, os, essid, ap])

print("Exporting...")
time.sleep(3)

print("Done !! Check 'CLIENTS.CSV' file. ")