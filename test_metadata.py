import json
import requests

from config import API_KEY, BASE_URL

url = f"{BASE_URL}/instruments/kpis/metadata?authKey={API_KEY}"

r = requests.get(url)
r.raise_for_status()

data = r.json()

print("Nycklar:", data.keys())
print()
print("Första posten:")
print(json.dumps(data["kpiHistoryMetadatas"][0], indent=2, ensure_ascii=False))