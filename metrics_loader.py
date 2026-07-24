from api import get_kpi
from models import Metrics


# KPI-ID:n
DIVIDEND_KPI = 1
PE_KPI = 2
PS_KPI = 3
PB_KPI = 4
EV_EBIT_KPI = 10
EV_EBITDA_KPI = 11
PEG_KPI = 19
ROIC_KPI = 37


def load_metrics(instrument_id):
    """
    Hämtar alla KPI:er som används av TradingLab och
    returnerar ett färdigt Metrics-objekt.
    """

    dividend_lookup = get_kpi(DIVIDEND_KPI)
    pe_lookup = get_kpi(PE_KPI)
    ps_lookup = get_kpi(PS_KPI)
    pb_lookup = get_kpi(PB_KPI)
    ev_ebit_lookup = get_kpi(EV_EBIT_KPI)
    ev_ebitda_lookup = get_kpi(EV_EBITDA_KPI)
    peg_lookup = get_kpi(PEG_KPI)
    roic_lookup = get_kpi(ROIC_KPI)

    return Metrics(
        dividend_yield=dividend_lookup.get(instrument_id),
        pe=pe_lookup.get(instrument_id),
        ps=ps_lookup.get(instrument_id),
        pb=pb_lookup.get(instrument_id),
        ev_ebit=ev_ebit_lookup.get(instrument_id),
        ev_ebitda=ev_ebitda_lookup.get(instrument_id),
        peg=peg_lookup.get(instrument_id),
        roic=roic_lookup.get(instrument_id),
    )