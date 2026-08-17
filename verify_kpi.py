from api import get_instrument, get_kpi


instrument = get_instrument("INVE B")

if instrument is None:
    print("Instrument hittades inte.")
else:
    instrument_id = instrument.id

    print(instrument_id)

    pe = get_kpi(2).get(instrument_id)

    print(pe)