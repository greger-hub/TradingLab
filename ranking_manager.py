from ranking import Ranking


class RankingManager:
    """
    Manages multiple independent rankings.

    Each ranking is identified by a name
    (for example: quality, value, total).
    """

    def __init__(self):
        self._rankings: dict[str, Ranking] = {}

    def get(self, name: str) -> Ranking:
        """
        Return a ranking.

        Creates it automatically if it does not exist.
        """
        if name not in self._rankings:
            self._rankings[name] = Ranking()

        return self._rankings[name]

    def add_score(
        self,
        ranking_name: str,
        instrument: str,
        score: float,
    ) -> None:
        """
        Add a company score to a ranking.
        """
        self.get(ranking_name).add(
            instrument=instrument,
            score=score,
        )

    def names(self) -> list[str]:
        """
        Return all ranking names.
        """
        return sorted(self._rankings.keys())

    def clear(self) -> None:
        """
        Clear every ranking.
        """
        for ranking in self._rankings.values():
            ranking.clear()