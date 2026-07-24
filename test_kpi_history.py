import json
import requests

from config import API_KEY, BASE_URL

instrument_id = 3   # Volvo
kpi_id = 1          # Direktavkastning

url = (
    f"{BASE_URL}/instruments/kpis/{kpi_id}/last/latest"
    f"?instList={instrument_id}&authKey={API_KEY}"
)

r = requests.get(url)
r.raise_for_status()

data = r.json()

print("Nycklar:", data.keys())
print()
print(json.dumps(data, indent=2, ensure_ascii=False)[:4000])