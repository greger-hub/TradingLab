from api import get_kpi


def main():
    print("Sök efter KPI-ID")

    while True:
        value = input("\nAnge KPI-ID (eller q för att avsluta): ").strip()

        if value.lower() == "q":
            break

        try:
            kpi_id = int(value)
        except ValueError:
            print("Ange ett heltal.")
            continue

        try:
            lookup = get_kpi(kpi_id)
        except Exception as e:
            print(f"Fel: {e}")
            continue

        print(f"Antal värden: {len(lookup)}")

        while True:
            instrument = input(
                "Instrument-ID (Enter för att välja nytt KPI): "
            ).strip()

            if instrument == "":
                break

            try:
                instrument_id = int(instrument)
            except ValueError:
                print("Ange ett heltal.")
                continue

            print(
                f"Värde: {lookup.get(instrument_id, 'Hittades inte')}"
            )


if __name__ == "__main__":
    main()