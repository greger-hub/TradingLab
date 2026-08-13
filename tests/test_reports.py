from models import AnalysisResult, Metrics, ScoreItem
from report import print_score_items


def test_print_score_items_outputs_title_and_score_details(capsys):
    result = AnalysisResult(
        score=45,
        metrics=Metrics(),
        score_items=[
            ScoreItem(
                name="Operating margin",
                points=20,
                max_points=25,
                comment="Strong operating margin",
            ),
            ScoreItem(
                name="Debt",
                points=15,
                max_points=25,
                comment="Acceptable debt",
            ),
        ],
    )

    print_score_items("QUALITY ANALYSIS", result)

    captured = capsys.readouterr()

    assert "QUALITY ANALYSIS" in captured.out
    assert "Operating margin" in captured.out
    assert "20.0/25" in captured.out
    assert "Strong operating margin" in captured.out
    assert "Debt" in captured.out
    assert "15.0/25" in captured.out
    assert "Acceptable debt" in captured.out


def test_print_score_items_handles_empty_score_items(capsys):
    result = AnalysisResult(
        score=0,
        metrics=Metrics(),
        score_items=[],
    )

    print_score_items("EMPTY ANALYSIS", result)

    captured = capsys.readouterr()

    assert "EMPTY ANALYSIS" in captured.out