from portfolio_entry import PortfolioEntry


class Portfolio:

    def __init__(self):
        self._entries: list[PortfolioEntry] = []

    @property
    def entries(self) -> list[PortfolioEntry]:
        return self._entries

    def add(self, instrument: str, score: float):
        self._entries.append(
            PortfolioEntry(
                instrument=instrument,
                score=score,
            )
        )

    def __len__(self):
        return len(self._entries)