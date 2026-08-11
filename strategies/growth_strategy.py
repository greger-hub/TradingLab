from api import get_kpi

from metrics import calculate_growth

from models import Metrics

from .base_strategy import BaseStrategy


PEG_KPI = 19


def score_revenue_growth(value):
    if value >= 20:
        return 1.0, "🚀 Exceptionell omsättningstillväxt"
    elif value >= 15:
        return 0.8, "✅ Stark omsättningstillväxt"
    elif value >= 10:
        return 0.6, "🟡 Bra omsättningstillväxt"
    elif value > 0:
        return 0.4, "🟡 Positiv omsättningstillväxt"
    else:
        return 0.2, "❌ Ingen eller negativ omsättningstillväxt"


def score_profit_growth(value):
    if value >= 20:
        return 1.0, "🚀 Exceptionell vinsttillväxt"
    elif value >= 15:
        return 0.8, "✅ Stark vinsttillväxt"
    elif value >= 10:
        return 0.6, "🟡 Bra vinsttillväxt"
    elif value > 0:
        return 0.4, "🟡 Positiv vinsttillväxt"
    else:
        return 0.2, "❌ Ingen eller negativ vinsttillväxt"


def score_peg(value):
    if value is None:
        return 0.0, "❓ PEG saknas"

    if value < 0:
        return 0.0, "⚠️ Negativ PEG kan inte bedömas"

    if value <= 1:
        return 1.0, "✅ Mycket attraktiv PEG"
    elif value <= 1.5:
        return 0.8, "✅ Attraktiv PEG"
    elif value <= 2:
        return 0.6, "🟡 Acceptabel PEG"
    else:
        return 0.2, "❌ Hög PEG"


class GrowthStrategy(BaseStrategy):
    """Strategi för att bedöma bolag med stark tillväxt."""

    def evaluate(
        self,
        current_report,
        previous_report,
        instrument_id,
    ):
        self.reset()

        peg = get_kpi(PEG_KPI).get(instrument_id)

        metrics = Metrics(
            revenue_growth=calculate_growth(
                current_report,
                previous_report,
                "revenues",
            ),
            profit_growth=calculate_growth(
                current_report,
                previous_report,
                "profit_To_Equity_Holders",
            ),
            peg=peg,
        )

        self.score(
            "Omsättningstillväxt",
            40,
            score_revenue_growth(
                metrics.revenue_growth,
            ),
        )

        self.score(
            "Vinsttillväxt",
            40,
            score_profit_growth(
                metrics.profit_growth,
            ),
        )

        if peg is not None:
            self.score(
                "PEG",
                20,
                score_peg(peg),
            )

        return self.build_result(metrics)