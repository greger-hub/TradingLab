from dataclasses import dataclass
from typing import Any

from models import AnalysisResult
from investment_strategy import InvestmentResult


@dataclass(frozen=True)
class ScreeningResult:
    """
    Complete analysis for one instrument.
    """

    instrument: dict[str, Any]
    latest_report: dict[str, Any]
    previous_report: dict[str, Any]

    quality: AnalysisResult
    value: AnalysisResult
    growth: AnalysisResult

    investment: InvestmentResult