from dataclasses import dataclass

from models import AnalysisResult


@dataclass
class InvestmentResult:
    quality_score: float
    value_score: float
    total_score: float


class InvestmentStrategy:

    def evaluate(
        self,
        quality_result: AnalysisResult,
        value_result: AnalysisResult,
    ) -> InvestmentResult:

        total = (
            quality_result.score +
            value_result.score
        ) / 2

        return InvestmentResult(
            quality_score=quality_result.score,
            value_score=value_result.score,
            total_score=total,
        )