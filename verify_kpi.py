from api import get_instrument, get_kpi

instrument = get_instrument("INVE B")

print(instrument["insId"])

pe = get_kpi(2).get(instrument["insId"])

print(pe)