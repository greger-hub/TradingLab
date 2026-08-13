from investment_strategy import InvestmentStrategy
from models import AnalysisResult, Metrics


def make_result(score):
    return AnalysisResult(
        score=score,
        metrics=Metrics(),
    )


def test_investment_strategy_calculates_average_score():
    strategy = InvestmentStrategy()

    result = strategy.evaluate(
        make_result(80),
        make_result(60),
        make_result(70),
    )

    assert result.quality_score == 80
    assert result.value_score == 60
    assert result.growth_score == 70
    assert result.total_score == 70


def test_investment_strategy_handles_zero_scores():
    strategy = InvestmentStrategy()

    result = strategy.evaluate(
        make_result(0),
        make_result(0),
        make_result(0),
    )

    assert result.total_score == 0


def test_investment_strategy_handles_maximum_scores():
    strategy = InvestmentStrategy()

    result = strategy.evaluate(
        make_result(100),
        make_result(100),
        make_result(100),
    )

    assert result.total_score == 100