from analysis import analyze_instrument
from ranking_manager import RankingManager
from screening_result import ScreeningResult


class Screener:
    """
    Analyze multiple instruments and collect the results.
    """

    def __init__(self):
        self._ranking_manager = RankingManager()
        self._results: list[ScreeningResult] = []

    @property
    def ranking_manager(self) -> RankingManager:
        return self._ranking_manager

    @property
    def results(self) -> list[ScreeningResult]:
        return self._results

    def analyze(self, tickers: list[str]) -> None:
        """
        Analyze every ticker in the list.
        """

        self._results.clear()
        self._ranking_manager.clear()

        for ticker in tickers:

            result = analyze_instrument(ticker)

            if result is None:
                continue

            self._results.append(result)

            name = result.instrument.get("name", ticker)

            self._ranking_manager.add_score(
                "quality",
                name,
                result.quality.score,
            )

            self._ranking_manager.add_score(
                "value",
                name,
                result.value.score,
            )

            self._ranking_manager.add_score(
                "growth",
                name,
                result.growth.score,
            )

            self._ranking_manager.add_score(
                "total",
                name,
                result.investment.total_score,
            )