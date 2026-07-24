from api import get_instrument, get_reports

from strategies.quality_strategy import QualityStrategy
from strategies.value_strategy import ValueStrategy

from investment_strategy import InvestmentStrategy

from screening_result import ScreeningResult

from report import print_report


def analyze_instrument(ticker: str) -> ScreeningResult | None:
    """
    Analyze a single instrument.

    Returns a ScreeningResult or None.
    """

    instrument = get_instrument(ticker)

    if instrument is None:
        return None

    instrument_id = instrument["insId"]

    reports = get_reports(instrument_id)

    if reports is None or len(reports) < 2:
        return None

    latest = reports[0]
    previous = reports[1]

    quality_result = QualityStrategy().evaluate(
        latest,
        previous,
        instrument_id,
    )

    value_result = ValueStrategy().evaluate(
        latest,
        previous,
        instrument_id,
    )

    investment_result = InvestmentStrategy().evaluate(
        quality_result,
        value_result,
    )

    return ScreeningResult(
        instrument=instrument,
        latest_report=latest,
        previous_report=previous,
        quality=quality_result,
        value=value_result,
        investment=investment_result,
    )


def run_analysis():
    """
    Run an interactive TradingLab analysis.
    """

    ticker = input("Vilken aktie vill du analysera? ").strip()

    result = analyze_instrument(ticker)

    if result is None:
        print("Analysen kunde inte genomföras.")
        return

    print_report(
        result.instrument,
        result.latest_report,
        result.previous_report,
        result.quality,
        result.value,
        result.investment,
    )


if __name__ == "__main__":
    run_analysis()