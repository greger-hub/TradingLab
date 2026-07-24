from api import get_instrument
from api import get_reports

instrument = get_instrument("INVE B")

reports = get_reports(instrument["insId"])

print(type(reports))
print(len(reports))
print(reports[0])