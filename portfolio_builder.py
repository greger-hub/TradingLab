from portfolio import Portfolio
from ranking_manager import RankingManager
from screening_result import ScreeningResult


class PortfolioBuilder:
    """
    Builds portfolios from rankings or screening results.
    """

    def __init__(
        self,
        ranking_manager: RankingManager,
    ):
        self._ranking_manager = ranking_manager

    def build(
        self,
        ranking: str = "total",
        size: int = 10,
    ) -> Portfolio:
        """
        Build a portfolio from a ranking.
        """

        portfolio = Portfolio()

        ranking_list = self._ranking_manager.get(ranking)

        for entry in ranking_list.top(size):
            portfolio.add(
                instrument=entry.instrument,
                score=entry.score,
            )

        return portfolio

    def build_from_results(
        self,
        results: list[ScreeningResult],
        size: int = 10,
    ) -> Portfolio:
        """
        Build a portfolio from screening results.
        """

        portfolio = Portfolio()

        for result in results[:size]:
            portfolio.add(
                instrument=result.instrument.name,
                score=result.quality.score,
            )

        return portfolio