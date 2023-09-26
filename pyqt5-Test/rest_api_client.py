import requests
import json

url = "https://localhost:5000/"  

with open('config.json', 'r') as config_file:
    config = json.load(config_file)
    
headers = {"Token": config["password"]}  # Ersetzen Sie dies durch das tatsächliche Token

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"GET-Anfrage erfolgreich: {data}")
else:
    print(f"Fehler bei der GET-Anfrage: {response.text}")

# PUT-Anfrage
new_data = {"value": "new_value"}

response = requests.put(url, json=new_data, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"PUT-Anfrage erfolgreich: {data}")
else:
    print(f"Fehler bei der PUT-Anfrage: {response.text}")
