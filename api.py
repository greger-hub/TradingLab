import requests
from config import BASE_URL, API_KEY


# Cachar instrumentlistan under programmets körning.
_instrument_cache = None

# Befintlig cache för KPI-data.
_kpi_cache = {}


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


def _load_instruments():
    """
    Hämtar hela instrumentlistan en gång per körning.
    Därefter används den lokala cachen.
    """

    global _instrument_cache

    if _instrument_cache is not None:
        return _instrument_cache

    data = _get("/instruments")
    _instrument_cache = data.get("instruments", [])

    return _instrument_cache


def _score_match(search, instrument):
    """
    Returnerar relevanspoäng.

    100 = exakt ticker
     95 = exakt företagsnamn
     90 = ticker börjar med söktext
     85 = första ordet i företagsnamnet börjar med söktext
     75 = annat ord i företagsnamnet börjar med söktext
      0 = ingen träff
    """

    ticker = instrument.get("ticker", "").upper()
    name = instrument.get("name", "").upper()

    if ticker == search:
        return 100

    if name == search:
        return 95

    if ticker.startswith(search):
        return 90

    words = name.split()

    if words:
        if words[0].startswith(search):
            return 85

        for word in words[1:]:
            if word.startswith(search):
                return 75

    return 0


def _find_matches(search_text):
    """
    Söker lokalt i den cachade instrumentlistan.
    """

    search = search_text.strip().upper()

    if len(search) < 3:
        raise ValueError("Söktexten måste innehålla minst 3 tecken.")

    instruments = _load_instruments()

    matches = []

    for instrument in instruments:
        score = _score_match(search, instrument)

        if score > 0:
            matches.append((score, instrument))

    matches.sort(
        key=lambda item: (
            -item[0],
            item[1].get("name", ""),
            item[1].get("ticker", "")
        )
    )

    unique = []
    seen = set()

    for score, instrument in matches:
        instrument_id = instrument.get("insId")

        if instrument_id in seen:
            continue

        seen.add(instrument_id)
        unique.append(instrument)

    return unique
def _choose_match(matches):
    """
    Returnerar valt instrument.

    - 0 träffar -> None
    - 1 träff  -> returneras direkt
    - >20 träffar -> be användaren förfina sökningen
    - 2-20 träffar -> användaren väljer
    """

    if not matches:
        print("\nInga instrument hittades.")
        return None

    if len(matches) == 1:
        instrument = matches[0]
        print(
            f"\nValt instrument: "
            f"{instrument['name']} ({instrument['ticker']})"
        )
        return instrument

    if len(matches) > 20:
        print(
            f"\nFör många träffar ({len(matches)}).\n"
            "Förfina sökningen genom att skriva fler tecken."
        )
        return None

    print("\nFlera träffar hittades:\n")

    for index, instrument in enumerate(matches, start=1):
        print(
            f"{index:2d}. "
            f"{instrument['name']:<35} "
            f"({instrument['ticker']})"
        )

    while True:
        choice = input(f"\nVälj [1-{len(matches)}]: ").strip()

        if not choice.isdigit():
            print("Ange ett nummer.")
            continue

        choice = int(choice)

        if 1 <= choice <= len(matches):
            return matches[choice - 1]

        print("Ogiltigt val.")


def get_instrument(search_text):
    """
    Söker fram ett instrument lokalt.
    """

    search = search_text.strip()

    if len(search) < 3:
        print("\nSöktexten är för kort.")
        print("Ange minst 3 tecken.")
        return None

    print(f"\nSöker efter: {search}")

    try:
        matches = _find_matches(search)
    except ValueError as error:
        print(error)
        return None

    return _choose_match(matches)
def get_reports(instrument_id, max_count=20):
    """
    Hämtar kvartalsrapporter för ett instrument.
    """

    data = _get(
        f"/instruments/{instrument_id}/reports",
        {
            "maxCount": max_count,
        },
    )

    return data.get("reportsQuarter", [])


def get_kpi(kpi_id):
    """
    Returnerar ett uppslagsverk:

        {
            instrument_id: kpi_värde
        }
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