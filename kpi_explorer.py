from api import (
    get_instrument,
    get_kpi,
    get_kpi_metadata,
)


def main():
    print("=== TradingLab KPI Explorer ===\n")

    ticker = input("Ange aktie: ").strip()

    instrument = get_instrument(ticker)

    if instrument is None:
        print("Aktien hittades inte.")
        return

    instrument_id = instrument.id

    print(f"\nBolag: {instrument.name}")
    print(f"Instrument-ID: {instrument_id}")

    try:
        start = int(input("\nFrån KPI-ID: "))
        end = int(input("Till KPI-ID: "))
    except ValueError:
        print("Ange heltal.")
        return

    print("\nHämtar KPI-metadata...")
    kpi_names = get_kpi_metadata()

    print("\n----- Resultat -----\n")

    found = 0

    for kpi_id in range(start, end + 1):
        try:
            lookup = get_kpi(kpi_id)
        except Exception:
            continue

        value = lookup.get(instrument_id)

        if value is None:
            continue

        name = kpi_names.get(kpi_id, "Okänd")

        print(f"{kpi_id:>3}  {name:<35} {value}")

        found += 1

    print("\n--------------------")
    print(f"Hittade {found} KPI:er.")
    print("--------------------")


if __name__ == "__main__":
    main()