from ranking import Ranking


def test_ranking_sorts_by_score_descending():
    ranking = Ranking()

    ranking.add("A", 70)
    ranking.add("B", 90)
    ranking.add("C", 80)

    assert [entry.instrument for entry in ranking.sorted()] == [
        "B",
        "C",
        "A",
    ]


def test_ranking_top_returns_highest_scores():
    ranking = Ranking()

    ranking.add("A", 70)
    ranking.add("B", 90)
    ranking.add("C", 80)

    assert [entry.instrument for entry in ranking.top(2)] == [
        "B",
        "C",
    ]


def test_ranking_returns_one_based_position():
    ranking = Ranking()

    ranking.add("A", 70)
    ranking.add("B", 90)
    ranking.add("C", 80)

    assert ranking.rank("B") == 1
    assert ranking.rank("C") == 2
    assert ranking.rank("A") == 3


def test_ranking_returns_none_for_unknown_instrument():
    ranking = Ranking()

    ranking.add("A", 70)

    assert ranking.rank("UNKNOWN") is None


def test_ranking_clear_removes_all_entries():
    ranking = Ranking()

    ranking.add("A", 70)
    ranking.add("B", 90)

    ranking.clear()

    assert len(ranking) == 0
    assert ranking.sorted() == []


def test_ranking_allows_duplicate_scores():
    ranking = Ranking()

    ranking.add("A", 80)
    ranking.add("B", 80)

    assert len(ranking) == 2
    assert [entry.instrument for entry in ranking.sorted()] == ["A", "B"]