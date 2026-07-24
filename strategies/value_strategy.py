from metrics_loader import get_kpi
from models import Metrics

from .base_strategy import BaseStrategy


DIVIDEND_KPI = 1
PE_KPI = 2
PS_KPI = 3
PB_KPI = 4
EV_EBIT_KPI = 10
EV_EBITDA_KPI = 11
PEG_KPI = 19
ROIC_KPI = 37


def score_pe(value):
    if value <= 10:
        return 20, "✅ Mycket låg P/E"
    elif value <= 15:
        return 16, "✅ Attraktiv P/E"
    elif value <= 20:
        return 12, "🟡 Rimlig P/E"
    else:
        return 6, "❌ Hög P/E"


def score_pb(value):
    if value <= 1:
        return 15, "✅ Mycket låg P/B"
    elif value <= 2:
        return 12, "✅ Attraktiv P/B"
    elif value <= 4:
        return 8, "🟡 Rimlig P/B"
    else:
        return 3, "❌ Hög P/B"


def score_ev_ebit(value):
    if value <= 10:
        return 20, "✅ Låg EV/EBIT"
    elif value <= 15:
        return 16, "🟡 Rimlig EV/EBIT"
    elif value <= 20:
        return 10, "🟡 Hög EV/EBIT"
    else:
        return 4, "❌ Mycket hög EV/EBIT"


def score_ev_ebitda(value):
    if value <= 8:
        return 15, "✅ Låg EV/EBITDA"
    elif value <= 12:
        return 12, "🟡 Rimlig EV/EBITDA"
    elif value <= 16:
        return 8, "🟡 Hög EV/EBITDA"
    else:
        return 3, "❌ Mycket hög EV/EBITDA"


def score_dividend(value):
    if value >= 5:
        return 15, "✅ Hög direktavkastning"
    elif value >= 3:
        return 12, "🟡 Bra direktavkastning"
    elif value >= 2:
        return 8, "🟡 Acceptabel direktavkastning"
    else:
        return 3, "❌ Låg direktavkastning"


def score_roic(value):
    if value >= 20:
        return 15, "✅ Exceptionell ROIC"
    elif value >= 15:
        return 12, "✅ Stark ROIC"
    elif value >= 10:
        return 8, "🟡 Bra ROIC"
    else:
        return 3, "❌ Svag ROIC"


class ValueStrategy(BaseStrategy):
    """Strategi för att bedöma om ett bolag är attraktivt värderat."""

    def evaluate(
        self,
        current_report,
        previous_report,
        instrument_id,
    ):
        self.reset()

        dividend = get_kpi(DIVIDEND_KPI).get(instrument_id)
        pe = get_kpi(PE_KPI).get(instrument_id)
        ps = get_kpi(PS_KPI).get(instrument_id)
        pb = get_kpi(PB_KPI).get(instrument_id)
        ev_ebit = get_kpi(EV_EBIT_KPI).get(instrument_id)
        ev_ebitda = get_kpi(EV_EBITDA_KPI).get(instrument_id)
        peg = get_kpi(PEG_KPI).get(instrument_id)
        roic = get_kpi(ROIC_KPI).get(instrument_id)

        metrics = Metrics(
            pe=pe,
            ps=ps,
            pb=pb,
            dividend_yield=dividend,
            ev_ebit=ev_ebit,
            ev_ebitda=ev_ebitda,
            roic=roic,
            peg=peg,
        )

        if pe is not None:
            self.score(
                "P/E",
                20,
                score_pe(pe),
            )

        if pb is not None:
            self.score(
                "P/B",
                15,
                score_pb(pb),
            )

        if ev_ebit is not None:
            self.score(
                "EV/EBIT",
                20,
                score_ev_ebit(ev_ebit),
            )

        if ev_ebitda is not None:
            self.score(
                "EV/EBITDA",
                15,
                score_ev_ebitda(ev_ebitda),
            )

        if dividend is not None:
            self.score(
                "Direktavkastning",
                15,
                score_dividend(dividend),
            )

        if roic is not None:
            self.score(
                "ROIC",
                15,
                score_roic(roic),
            )

        return self.build_result(metrics)