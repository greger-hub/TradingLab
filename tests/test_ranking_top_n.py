from ranking import Ranking


def make_ranking():
    ranking = Ranking()

    ranking.add("Volvo", 88.5)
    ranking.add("Investor", 94.0)
    ranking.add("Atlas Copco", 96.5)
    ranking.add("Lifco", 92.0)

    return ranking


def test_ranking_can_return_top_one():
    ranking = make_ranking()

    result = ranking.top(1)

    assert len(result) == 1
    assert result[0].instrument == "Atlas Copco"


def test_ranking_can_return_top_two():
    ranking = make_ranking()

    result = ranking.top(2)

    assert [entry.instrument for entry in result] == [
        "Atlas Copco",
        "Investor",
    ]


def test_ranking_can_return_top_three():
    ranking = make_ranking()

    result = ranking.top(3)

    assert [entry.instrument for entry in result] == [
        "Atlas Copco",
        "Investor",
        "Lifco",
    ]


def test_ranking_returns_all_when_limit_is_larger_than_ranking():
    ranking = make_ranking()

    result = ranking.top(10)

    assert len(result) == 4


def test_ranking_returns_empty_when_limit_is_zero():
    ranking = make_ranking()

    result = ranking.top(0)

    assert result == []