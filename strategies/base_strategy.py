from abc import ABC, abstractmethod

from models import AnalysisResult, Metrics, ScoreItem


class BaseStrategy(ABC):
    """
    Basklass för alla analysstrategier.
    Hanterar poäng, kommentarer och ScoreItems.
    """

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._score = 0.0
        self._comments: list[str] = []
        self._score_items: list[ScoreItem] = []

    def add_score(
        self,
        name: str,
        points: float,
        max_points: float,
        comment: str,
    ) -> None:
        """
        Lägger till en poängpost och uppdaterar totalsumman.
        """

        self._score += points
        self._comments.append(comment)

        self._score_items.append(
            ScoreItem(
                name=name,
                points=points,
                max_points=max_points,
                comment=comment,
            )
        )

    def score(
        self,
        name: str,
        max_points: float,
        result: tuple[float, str],
    ) -> None:
        """
        Tar emot resultatet från en score_*()-funktion.

        score_*()-funktionerna returnerar:
            (ratio, comment)

        där ratio är ett värde mellan 0.0 och 1.0.
        Här omvandlas ratio till faktiska poäng med hjälp av max_points.
        """

        ratio, comment = result
        points = ratio * max_points

        self.add_score(
            name=name,
            points=points,
            max_points=max_points,
            comment=comment,
        )

    def build_result(
        self,
        metrics: Metrics,
    ) -> AnalysisResult:
        """
        Bygger ett färdigt AnalysisResult.
        """

        return AnalysisResult(
            score=self._score,
            metrics=metrics,
            comments=self._comments.copy(),
            score_items=self._score_items.copy(),
        )

    @abstractmethod
    def evaluate(
        self,
        current_report,
        previous_report,
        instrument_id,
    ):
        """
        Returnerar ett AnalysisResult.
        """
        raise NotImplementedError