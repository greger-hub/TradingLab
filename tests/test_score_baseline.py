import pytest

from score import score_debt, score_growth, score_margin, score_roe


@pytest.mark.parametrize(
    ("value", "expected_points"),
    [
        (20, 25),
        (15, 20),
        (10, 15),
        (9.99, 5),
    ],
)
def test_score_margin_boundaries(value, expected_points):
    points, _ = score_margin(value)
    assert points == expected_points
    assert 0 <= points <= 25


@pytest.mark.parametrize(
    ("value", "expected_points"),
    [
        (0.49, 25),
        (0.5, 20),
        (0.99, 20),
        (1.0, 10),
    ],
)
def test_score_debt_boundaries(value, expected_points):
    points, _ = score_debt(value)
    assert points == expected_points
    assert 0 <= points <= 25


@pytest.mark.parametrize(
    ("value", "expected_points"),
    [
        (20, 25),
        (15, 20),
        (10, 15),
        (9.99, 5),
    ],
)
def test_score_roe_boundaries(value, expected_points):
    points, _ = score_roe(value)
    assert points == expected_points
    assert 0 <= points <= 25


@pytest.mark.parametrize(
    ("revenue_growth", "profit_growth", "expected_points"),
    [
        (15, 15, 25),
        (10, 10, 20),
        (5, 5, 15),
        (1, 1, 10),
        (0, 0, 0),
        (-5, -5, 0),
    ],
)
def test_score_growth_boundaries(
    revenue_growth,
    profit_growth,
    expected_points,
):
    points, _ = score_growth(revenue_growth, profit_growth)
    assert points == expected_points
    assert 0 <= points <= 25


def test_score_growth_maximum_is_25():
    points, comment = score_growth(100, 100)
    assert points == 25
    assert "Mycket stark" in comment