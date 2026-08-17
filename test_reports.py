from api import get_instrument
from api import get_reports


instrument = get_instrument("INVE B")

if instrument is None:
    print("Instrument hittades inte.")
else:
    reports = get_reports(instrument.id)

    print(type(reports))
    print(len(reports))

    if reports:
        print(reports[0])