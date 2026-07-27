from api import get_kpi

from metrics import (
    calculate_operating_margin,
    calculate_debt_ratio,
    calculate_equity_ratio,
    calculate_roe,
    calculate_growth,
)

from models import Metrics

from .base_strategy import BaseStrategy


ROIC_KPI = 37


def score_margin(value):
    if value >= 20:
        return 1.0, "✅ Mycket hög rörelsemarginal"
    elif value >= 15:
        return 0.8, "✅ Stark rörelsemarginal"
    elif value >= 10:
        return 0.6, "🟡 Godkänd rörelsemarginal"
    else:
        return 0.2, "❌ Låg rörelsemarginal"


def score_debt(value):
    if value < 0.5:
        return 1.0, "✅ Låg skuldsättning"
    elif value < 1.0:
        return 0.8, "🟡 Acceptabel skuldsättning"
    else:
        return 0.4, "❌ Hög skuldsättning"


def score_equity_ratio(value):
    if value is None:
        return 0.0, "❓ Soliditet saknas"

    if value >= 50:
        return 1.0, "✅ Mycket stark soliditet"
    elif value >= 40:
        return 0.8, "✅ Stark soliditet"
    elif value >= 30:
        return 0.6, "🟡 Godkänd soliditet"
    else:
        return 0.2, "❌ Låg soliditet"


def score_roe(value):
    if value >= 20:
        return 1.0, "✅ Mycket hög ROE"
    elif value >= 15:
        return 0.8, "✅ Stark ROE"
    elif value >= 10:
        return 0.6, "🟡 Godkänd ROE"
    else:
        return 0.2, "❌ Låg ROE"


def score_roic(value):
    if value is None:
        return 0.0, "❓ ROIC saknas"

    if value >= 20:
        return 1.0, "✅ Exceptionell ROIC"
    elif value >= 15:
        return 0.8, "✅ Stark ROIC"
    elif value >= 10:
        return 0.6, "🟡 Bra ROIC"
    else:
        return 0.2, "❌ Svag ROIC"


def score_growth(revenue_growth, profit_growth):
    ratio = 0.0

    for growth in (revenue_growth, profit_growth):
        if growth >= 15:
            ratio += 0.5
        elif growth >= 10:
            ratio += 0.4
        elif growth >= 5:
            ratio += 0.3
        elif growth > 0:
            ratio += 0.2

    if ratio >= 0.8:
        comment = "📈 Mycket stark tillväxt"
    elif ratio >= 0.6:
        comment = "📈 God tillväxt"
    elif ratio > 0:
        comment = "📈 Svag men positiv tillväxt"
    else:
        comment = "📉 Ingen eller negativ tillväxt"

    return ratio, comment


class QualityStrategy(BaseStrategy):
    """Strategi för att bedöma kvalitetsbolag."""

    def evaluate(
        self,
        current_report,
        previous_report,
        instrument_id,
    ):
        self.reset()

        roic = get_kpi(ROIC_KPI).get(instrument_id)

        metrics = Metrics(
            operating_margin=calculate_operating_margin(current_report),
            debt_ratio=calculate_debt_ratio(current_report),
            equity_ratio=calculate_equity_ratio(current_report),
            roe=calculate_roe(current_report),
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
            roic=roic,
        )

        self.score(
            "Rörelsemarginal",
            20,
            score_margin(metrics.operating_margin),
        )

        self.score(
            "Skuldsättning",
            15,
            score_debt(metrics.debt_ratio),
        )

        self.score(
            "Soliditet",
            15,
            score_equity_ratio(metrics.equity_ratio),
        )

        self.score(
            "ROE",
            20,
            score_roe(metrics.roe),
        )

        self.score(
            "ROIC",
            20,
            score_roic(metrics.roic),
        )

        self.score(
            "Tillväxt",
            10,
            score_growth(
                metrics.revenue_growth,
                metrics.profit_growth,
            ),
        )

        return self.build_result(metrics)