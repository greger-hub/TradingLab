from models import AnalysisResult, Metrics, ScoreItem


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