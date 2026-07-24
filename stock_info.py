import os

import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BORSDATA_API_KEY")

ticker = "ATCO A"

url = f"https://apiservice.borsdata.se/v1/instruments?authKey={API_KEY}"

data = requests.get(url).json()

for stock in data["instruments"]:

    if stock["ticker"] == ticker:

        print("Bolag:", stock["name"])

        print("Ticker:", stock["ticker"])

        print("ISIN:", stock["isin"])

        print("Bransch-ID:", stock["branchId"])

        print("Sektor-ID:", stock["sectorId"])

        break