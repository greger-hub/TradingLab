import requests
import json

from config import BASE_URL, API_KEY

url = f"{BASE_URL}/instruments/kpis/2/last/latest"

response = requests.get(
    url,
    params={"authKey": API_KEY},
    timeout=30,
)

data = response.json()

print("Typ:", type(data))

if isinstance(data, dict):
    print("Nycklar:", data.keys())

    for key, value in data.items():
        if isinstance(value, list):
            print(f"\nLista '{key}' innehåller {len(value)} objekt")
            print("\nFörsta objektet:")
            print(json.dumps(value[0], indent=2))
            break