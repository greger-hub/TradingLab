from abc import ABC, abstractmethod

from portfolio import Portfolio
from portfolio_builder import PortfolioBuilder
from screener import Screener


class BasePortfolioStrategy(ABC):
    """
    Base class for all portfolio strategies.
    """

    name = "Base Strategy"
    description = ""

    @abstractmethod
    def build(
        self,
        screener: Screener,
        size: int = 10,
    ) -> Portfolio:
        raise NotImplementedError

    def _builder(
        self,
        screener: Screener,
    ) -> PortfolioBuilder:
        return PortfolioBuilder(
            screener.ranking_manager,
        )