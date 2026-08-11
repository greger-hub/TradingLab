from dataclasses import dataclass

from models import AnalysisResult


@dataclass
class InvestmentResult:
    quality_score: float
    value_score: float
    growth_score: float
    total_score: float


class InvestmentStrategy:

    def evaluate(
        self,
        quality_result: AnalysisResult,
        value_result: AnalysisResult,
        growth_result: AnalysisResult,
    ) -> InvestmentResult:

        total = (
            quality_result.score +
            value_result.score +
            growth_result.score
        ) / 3

        return InvestmentResult(
            quality_score=quality_result.score,
            value_score=value_result.score,
            growth_score=growth_result.score,
            total_score=total,
        )