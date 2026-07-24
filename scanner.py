import os

import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BORSDATA_API_KEY")

url = f"https://apiservice.borsdata.se/v1/instruments?authKey={API_KEY}"

response = requests.get(url)

data = response.json()

print("Svenska aktier:\n")

for aktie in data["instruments"][:20]:

    print(f"{aktie['ticker']:8} {aktie['name']}")