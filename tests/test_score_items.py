from models import AnalysisResult, Metrics, ScoreItem
from score import calculate_score


def test_score_item_contains_transparent_scoring_detail():
    item = ScoreItem(
        name="Operating margin",
        points=25,
        max_points=25,
        comment="Very high operating margin",
    )

    assert item.name == "Operating margin"
    assert item.points == 25
    assert item.max_points == 25
    assert item.comment == "Very high operating margin"


def test_analysis_result_can_contain_score_items():
    item = ScoreItem(
        name="ROE",
        points=20,
        max_points=25,
        comment="Strong ROE",
    )

    result = AnalysisResult(
        score=20,
        metrics=Metrics(),
        score_items=[item],
    )

    assert len(result.score_items) == 1
    assert result.score_items[0].name == "ROE"
    assert result.score_items[0].points == 20
    assert result.score_items[0].max_points == 25


def test_calculate_score_populates_score_items():
    current_report = {
        "revenues": 120,
        "profit_To_Equity_Holders": 24,
        "operating_Income": 24,
        "net_Debt": 30,
        "total_Equity": 100,
    }

    previous_report = {
        "revenues": 100,
        "profit_To_Equity_Holders": 20,
        "operating_Income": 20,
        "net_Debt": 30,
        "total_Equity": 100,
    }

    result = calculate_score(current_report, previous_report)

    assert len(result.score_items) == 4

    assert [item.name for item in result.score_items] == [
        "Operating margin",
        "Debt",
        "ROE",
        "Growth",
    ]

    assert all(item.max_points == 25 for item in result.score_items)
    assert sum(item.points for item in result.score_items) == result.score


def test_calculate_score_items_reflect_zero_growth():
    current_report = {
        "revenues": 100,
        "profit_To_Equity_Holders": 20,
        "operating_Income": 20,
        "net_Debt": 30,
        "total_Equity": 100,
    }

    previous_report = {
        "revenues": 100,
        "profit_To_Equity_Holders": 20,
        "operating_Income": 20,
        "net_Debt": 30,
        "total_Equity": 100,
    }

    result = calculate_score(current_report, previous_report)

    growth_item = result.score_items[3]

    assert growth_item.name == "Growth"
    assert growth_item.points == 0
    assert growth_item.max_points == 25
    assert "Ingen eller negativ tillväxt" in growth_item.comment


def test_calculate_score_items_reflect_maximum_scores():
    current_report = {
        "revenues": 120,
        "profit_To_Equity_Holders": 24,
        "operating_Income": 24,
        "net_Debt": 10,
        "total_Equity": 100,
    }

    previous_report = {
        "revenues": 100,
        "profit_To_Equity_Holders": 20,
        "operating_Income": 20,
        "net_Debt": 10,
        "total_Equity": 100,
    }

    result = calculate_score(current_report, previous_report)

    assert len(result.score_items) == 4
    assert all(item.max_points == 25 for item in result.score_items)

    assert result.score_items[0].points == 25
    assert result.score_items[1].points == 25
    assert result.score_items[2].points == 25
    assert result.score_items[3].points == 25

    assert result.score == 100