import requests

import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BORSDATA_API_KEY")

url = f"https://apiservice.borsdata.se/v1/instruments?authKey={API_KEY}"

data = requests.get(url).json()

def get_stock(ticker):

    for stock in data["instruments"]:

        if stock["ticker"].upper() == ticker.upper():

            return stock

    return None

ticker = input("Vilken aktie vill du analysera? ")

stock = get_stock(ticker)

if stock:

    print("\nBolag:", stock["name"])

    print("Ticker:", stock["ticker"])

    print("ISIN:", stock["isin"])

    print("Bransch-ID:", stock["branchId"])

    print("Sektor-ID:", stock["sectorId"])

else:

    print("Aktien hittades inte.")