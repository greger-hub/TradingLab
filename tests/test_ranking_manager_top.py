from ranking_manager import RankingManager


def make_manager():
    manager = RankingManager()

    manager.add_score("quality", "Volvo", 88.5)
    manager.add_score("quality", "Investor", 94.0)
    manager.add_score("quality", "Atlas Copco", 96.5)
    manager.add_score("quality", "Lifco", 92.0)

    manager.add_score("growth", "Volvo", 70.0)
    manager.add_score("growth", "Investor", 85.0)
    manager.add_score("growth", "Atlas Copco", 90.0)

    return manager


def test_manager_can_return_top_n_for_quality():
    manager = make_manager()

    result = manager.top("quality", 2)

    assert [entry.instrument for entry in result] == [
        "Atlas Copco",
        "Investor",
    ]


def test_manager_can_return_top_n_for_growth():
    manager = make_manager()

    result = manager.top("growth", 2)

    assert [entry.instrument for entry in result] == [
        "Atlas Copco",
        "Investor",
    ]


def test_manager_returns_all_when_limit_is_larger_than_ranking():
    manager = make_manager()

    result = manager.top("quality", 10)

    assert len(result) == 4


def test_manager_returns_empty_for_unknown_ranking():
    manager = make_manager()

    result = manager.top("momentum", 10)

    assert result == []


def test_manager_returns_empty_when_limit_is_zero():
    manager = make_manager()

    result = manager.top("quality", 0)

    assert result == []