from unittest.mock import patch

from models import AnalysisResult, Metrics
from investment_strategy import InvestmentResult
from screening_result import ScreeningResult
from screener import Screener


def make_result(
    name,
    quality_score,
    value_score,
    growth_score,
    total_score,
):
    return ScreeningResult(
        instrument={"name": name},
        latest_report={},
        previous_report={},
        quality=AnalysisResult(
            score=quality_score,
            metrics=Metrics(),
        ),
        value=AnalysisResult(
            score=value_score,
            metrics=Metrics(),
        ),
        growth=AnalysisResult(
            score=growth_score,
            metrics=Metrics(),
        ),
        investment=InvestmentResult(
            quality_score=quality_score,
            value_score=value_score,
            growth_score=growth_score,
            total_score=total_score,
        ),
    )


def test_screener_creates_all_strategy_rankings():
    results = [
        make_result("Investor", 90, 80, 70, 80),
        make_result("Volvo", 80, 90, 60, 77),
    ]

    with patch(
        "screener.analyze_instrument",
        side_effect=results,
    ):
        screener = Screener()
        screener.analyze(["Investor", "Volvo"])

    assert screener.ranking_manager.names() == [
        "growth",
        "quality",
        "total",
        "value",
    ]


def test_screener_adds_growth_scores_to_growth_ranking():
    results = [
        make_result("Investor", 90, 80, 70, 80),
        make_result("Volvo", 80, 90, 60, 77),
    ]

    with patch(
        "screener.analyze_instrument",
        side_effect=results,
    ):
        screener = Screener()
        screener.analyze(["Investor", "Volvo"])

    growth_ranking = screener.ranking_manager.get("growth")

    assert [entry.instrument for entry in growth_ranking.top(2)] == [
        "Investor",
        "Volvo",
    ]