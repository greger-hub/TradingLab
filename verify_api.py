import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BORSDATA_API_KEY")

if not API_KEY:
    raise RuntimeError("BORSDATA_API_KEY saknas i .env")

BASE_URL = "https://apiservice.borsdata.se/v1"


def call(endpoint, params=None):
    params = params or {}
    params["authKey"] = API_KEY

    url = f"{BASE_URL}/{endpoint}"

    print("=" * 80)
    print("GET:", url)
    print("PARAMS:", params)

    response = requests.get(url, params=params, timeout=30)

    print("STATUS:", response.status_code)

    if not response.ok:
        print(response.text)
        return None

    data = response.json()

    print(json.dumps(data, indent=2, ensure_ascii=False)[:5000])
    print()

    return data


def main():
    instrument = call("instruments", {"search": "Volvo"})

    instrument_id = None

    if instrument and instrument.get("instruments"):
        instrument_id = instrument["instruments"][0]["insId"]
        print(f"Instrument ID: {instrument_id}")

    if not instrument_id:
        print("Kunde inte hitta något instrument.")
        return

    call(f"instruments/{instrument_id}/reports")

    call("instruments/kpis/metadata")

    call("instruments/kpis/1/last/latest")


if __name__ == "__main__":
    main()