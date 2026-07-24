import requests

import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BORSDATA_API_KEY")

ticker = input("Vilken aktie? ").upper()

# Hämta alla instrument

url = f"https://apiservice.borsdata.se/v1/instruments?authKey={API_KEY}"

data = requests.get(url).json()

instrument = None

for stock in data["instruments"]:

    if stock["ticker"].upper() == ticker:

        instrument = stock

        break

if instrument is None:

    print("Aktien hittades inte.")

    exit()

print("\n======================")

print(instrument["name"])

print("======================")

print("Ticker:", instrument["ticker"])

print("ISIN:", instrument["isin"])

print("Instrument-ID:", instrument["insId"])