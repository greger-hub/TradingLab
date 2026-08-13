from analysis import analyze_instrument


def test_analyze_instrument_builds_complete_result(monkeypatch):

    monkeypatch.setattr(
        "analysis.get_instrument",
        lambda ticker: {
            "name": "Test Company",
            "insId": 1,
        },
    )

    monkeypatch.setattr(
        "analysis.get_reports",
        lambda instrument_id: [
            {
                "year": 2025,
                "revenues": 120,
                "profit_To_Equity_Holders": 24,
                "operating_Income": 24,
                "net_Debt": 20,
                "total_Equity": 100,
            },
            {
                "year": 2024,
                "revenues": 100,
                "profit_To_Equity_Holders": 20,
                "operating_Income": 20,
                "net_Debt": 20,
                "total_Equity": 100,
            },
        ],
    )

    monkeypatch.setattr(
        "strategies.quality_strategy.get_kpi",
        lambda _: {1: 20},
    )

    monkeypatch.setattr(
        "strategies.value_strategy.get_kpi",
        lambda _: {1: 10},
    )

    monkeypatch.setattr(
        "strategies.growth_strategy.get_kpi",
        lambda _: {1: 1},
    )

    result = analyze_instrument("TEST")

    assert result is not None

    assert result.instrument["name"] == "Test Company"

    assert result.quality.score_items
    assert result.value.score_items
    assert result.growth.score_items

    assert result.investment.total_score > 0