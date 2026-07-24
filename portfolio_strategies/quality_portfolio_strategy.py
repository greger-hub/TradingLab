from portfolio import Portfolio
from screener import Screener

from portfolio_strategies.base_portfolio_strategy import (
    BasePortfolioStrategy,
)


class QualityPortfolioStrategy(BasePortfolioStrategy):

    name = "Quality Portfolio"

    description = (
        "Builds a portfolio from the highest quality companies."
    )

def build(
    self,
    screener: Screener,
    size: int = 10,
) -> Portfolio:

    results = sorted(
        screener.results,
        key=lambda result: result.quality.score,
        reverse=True,
    )

    return self._builder(
        screener,
    ).build_from_results(
        results,
        size=size,
    )