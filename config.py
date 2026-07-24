from dotenv import load_dotenv

import os

# Ladda .env

load_dotenv()

# API-nyckel

API_KEY = os.getenv("BORSDATA_API_KEY")

# Börsdata API

BASE_URL = "https://apiservice.borsdata.se/v1"

# Kontrollera att nyckeln finns

if API_KEY is None:

    raise ValueError("BORSDATA_API_KEY saknas i .env")
