from strategies.quality_strategy import QualityStrategy
from strategies.value_strategy import ValueStrategy
from strategies.growth_strategy import GrowthStrategy


def fake_report():
    return {
        "revenues": 120,
        "profit_To_Equity_Holders": 24,
        "operating_Income": 24,
        "net_Debt": 20,
        "total_Equity": 100,
    }


def previous_report():
    return {
        "revenues": 100,
        "profit_To_Equity_Holders": 20,
        "operating_Income": 20,
        "net_Debt": 20,
        "total_Equity": 100,
    }


def test_quality_strategy_returns_score_items():
    strategy = QualityStrategy()

    result = strategy.evaluate(
        fake_report(),
        previous_report(),
        1,
    )

    assert len(result.score_items) > 0
    assert result.score == sum(
        item.points for item in result.score_items
    )


def test_value_strategy_returns_score_items(monkeypatch):
    monkeypatch.setattr(
        "strategies.value_strategy.get_kpi",
        lambda _: {1: 10},
    )

    strategy = ValueStrategy()

    result = strategy.evaluate(
        fake_report(),
        previous_report(),
        1,
    )

    assert len(result.score_items) > 0


def test_growth_strategy_returns_score_items(monkeypatch):
    monkeypatch.setattr(
        "strategies.growth_strategy.get_kpi",
        lambda _: {1: 1},
    )

    strategy = GrowthStrategy()

    result = strategy.evaluate(
        fake_report(),
        previous_report(),
        1,
    )

    assert len(result.score_items) > 0