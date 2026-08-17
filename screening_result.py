from dataclasses import dataclass

from models import AnalysisResult, Instrument
from investment_strategy import InvestmentResult


@dataclass(frozen=True)
class ScreeningResult:
    """
    Complete analysis for one provider-independent instrument.
    """

    instrument: Instrument
    latest_report: dict
    previous_report: dict

    quality: AnalysisResult
    value: AnalysisResult
    growth: AnalysisResult

    investment: InvestmentResult