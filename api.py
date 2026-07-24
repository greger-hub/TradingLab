import requests
from config import BASE_URL, API_KEY


def _get(endpoint, params=None):
    if params is None:
        params = {}

    params = params.copy()
    params["authKey"] = API_KEY

    response = requests.get(
        f"{BASE_URL}{endpoint}",
        params=params,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def get_instrument(search_text):
    data = _get(
        "/instruments",
        {
            "query": search_text,
        },
    )

    instruments = data.get("instruments", [])

    if not instruments:
        return None

    search = search_text.upper()

    for instrument in instruments:
        if instrument["ticker"].upper() == search:
            return instrument

    return instruments[0]


def get_reports(instrument_id, max_count=20):
    data = _get(
        f"/instruments/{instrument_id}/reports",
        {
            "maxCount": max_count,
        },
    )

    return data.get("reportsQuarter", [])
_kpi_cache = {}


def get_kpi(kpi_id):
    """
    Returnerar ett uppslagsverk:
        { instrument_id: kpi_värde }
    """

    if kpi_id in _kpi_cache:
        return _kpi_cache[kpi_id]

    data = _get(
        f"/instruments/kpis/{kpi_id}/last/latest"
    )

    lookup = {}

    for row in data.get("values", []):
        lookup[row["i"]] = row["n"]

    _kpi_cache[kpi_id] = lookup

    return lookup