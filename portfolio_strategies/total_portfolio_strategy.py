from portfolio import Portfolio

from portfolio_strategies.base_portfolio_strategy import (
    BasePortfolioStrategy,
)

from screener import Screener


class TotalPortfolioStrategy(BasePortfolioStrategy):
    """
    Portfolio based on the total ranking.
    """

    name = "Total Portfolio"

    description = (
        "Builds a portfolio from the highest "
        "ranked companies."
    )

    def build(
        self,
        screener: Screener,
        size: int = 10,
    ) -> Portfolio:

        return self._builder(
            screener,
        ).build(
            ranking="total",
            size=size,
        )