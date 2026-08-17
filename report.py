from models import AnalysisResult, Instrument
from investment_strategy import InvestmentResult


def print_score_items(title: str, result: AnalysisResult):
    """
    Skriver ut poängfördelningen för en strategi.
    """

    print(f"\n============= {title} =============")

    for item in result.score_items:
        print(
            f"{item.name:<20}"
            f"{item.points:>5.1f}/{item.max_points:<4.0f}  "
            f"{item.comment}"
        )


def print_report(
    instrument: Instrument,
    latest: dict,
    previous: dict,
    quality_result: AnalysisResult,
    value_result: AnalysisResult,
    growth_result: AnalysisResult,
    investment_result: InvestmentResult,
):
    """
    Skriver ut en komplett TradingLab-analys.
    """

    print("\n================================================")
    print(f"TradingLab Analysis - {instrument.name}")
    print("================================================")

    print(f"Senaste år: {latest['year']}")
    print(f"Föregående år: {previous['year']}")

    print(f"\nOmsättning: {latest['revenues']:,.0f} MSEK")
    print(f"Rörelseresultat: {latest['operating_Income']:,.0f} MSEK")
    print(f"Vinst: {latest['profit_To_Equity_Holders']:,.0f} MSEK")
    print(f"Vinst per aktie: {latest['earnings_Per_Share']:.2f} kr")

    #
    # QUALITY
    #

    print("\n================ QUALITY ================")

    qm = quality_result.metrics

    if qm.operating_margin is not None:
        print(f"Rörelsemarginal: {qm.operating_margin:.1f}%")

    if qm.debt_ratio is not None:
        print(f"Skuldsättningsgrad: {qm.debt_ratio:.2f}")

    if qm.equity_ratio is not None:
        print(f"Soliditet: {qm.equity_ratio:.1f}%")

    if qm.roe is not None:
        print(f"ROE: {qm.roe:.1f}%")

    if qm.revenue_growth is not None:
        print(f"Omsättningstillväxt: {qm.revenue_growth:.1f}%")

    if qm.profit_growth is not None:
        print(f"Vinsttillväxt: {qm.profit_growth:.1f}%")

    print(f"\nQuality Score: {investment_result.quality_score:.1f}/100")

    #
    # VALUE
    #

    print("\n================ VALUE ==================")

    vm = value_result.metrics

    if vm.pe is not None:
        print(f"P/E: {vm.pe:.2f}")

    if vm.ps is not None:
        print(f"P/S: {vm.ps:.2f}")

    if vm.pb is not None:
        print(f"P/B: {vm.pb:.2f}")

    if vm.dividend_yield is not None:
        print(f"Direktavkastning: {vm.dividend_yield:.2f}%")

    if vm.ev_ebit is not None:
        print(f"EV/EBIT: {vm.ev_ebit:.2f}")

    if vm.ev_ebitda is not None:
        print(f"EV/EBITDA: {vm.ev_ebitda:.2f}")

    if vm.roic is not None:
        print(f"ROIC: {vm.roic:.2f}%")

    if vm.peg is not None:
        print(f"PEG: {vm.peg:.2f}")

    print(f"\nValue Score: {investment_result.value_score:.1f}/100")

    #
    # GROWTH
    #

    print("\n================ GROWTH =================")

    gm = growth_result.metrics

    if gm.revenue_growth is not None:
        print(f"Omsättningstillväxt: {gm.revenue_growth:.1f}%")

    if gm.profit_growth is not None:
        print(f"Vinsttillväxt: {gm.profit_growth:.1f}%")

    if gm.peg is not None:
        print(f"PEG: {gm.peg:.2f}")

    if hasattr(investment_result, "growth_score"):
        print(f"\nGrowth Score: {investment_result.growth_score:.1f}/100")

    #
    # ANALYS
    #

    print_score_items("QUALITY ANALYSIS", quality_result)
    print_score_items("VALUE ANALYSIS", value_result)
    print_score_items("GROWTH ANALYSIS", growth_result)

    #
    # TOTAL
    #

    print("\n================================================")
    print(f"TradingLab Score: {investment_result.total_score:.1f}/100")
    print("================================================")