from dataclasses import dataclass


@dataclass(frozen=True)
class RankingEntry:
    """
    Represents one ranked company.
    """
    instrument: str
    score: float


class Ranking:
    """
    Generic ranking engine.

    Stores a list of companies and their scores and can:
    - sort them
    - return Top N
    - return a company's rank
    """

    def __init__(self):
        self._entries: list[RankingEntry] = []

    def add(self, instrument: str, score: float) -> None:
        """
        Add a company score.
        """
        self._entries.append(
            RankingEntry(
                instrument=instrument,
                score=score,
            )
        )

    def sorted(self) -> list[RankingEntry]:
        """
        Return all entries sorted by descending score.
        """
        return sorted(
            self._entries,
            key=lambda entry: entry.score,
            reverse=True,
        )

    def top(self, limit: int = 10) -> list[RankingEntry]:
        """
        Return the highest ranked companies.
        """
        return self.sorted()[:limit]

    def rank(self, instrument: str) -> int | None:
        """
        Return ranking position (1-based).

        Returns None if company is not found.
        """
        for position, entry in enumerate(self.sorted(), start=1):
            if entry.instrument == instrument:
                return position

        return None

    def clear(self) -> None:
        """
        Remove all ranking entries.
        """
        self._entries.clear()

    def __len__(self) -> int:
        return len(self._entries)