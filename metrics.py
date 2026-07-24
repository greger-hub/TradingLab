def calculate_operating_margin(report):

    """Beräkna rörelsemarginal i procent."""

    if report["revenues"] == 0:

        return 0

    return report["operating_Income"] / report["revenues"] * 100

def calculate_debt_ratio(report):

    """Beräkna skuldsättningsgrad."""

    if report["total_Equity"] == 0:

        return 0

    return report["net_Debt"] / report["total_Equity"]

def calculate_roe(report):

    """Beräkna avkastning på eget kapital."""

    if report["total_Equity"] == 0:

        return 0

    return (

        report["profit_To_Equity_Holders"]

        / report["total_Equity"]

        * 100

    )

def calculate_growth(current, previous, field):

    """Beräknar procentuell tillväxt mellan två rapporter."""

    previous_value = previous[field]

    if previous_value == 0:

        return 0

    current_value = current[field]

    return (

        (current_value - previous_value)

        / previous_value

        * 100

    )

def calculate_equity_ratio(report):

    """Beräknar soliditet i procent."""

    total_assets = report.get("total_Assets", 0)

    if total_assets == 0:

        return 0

    return report["total_Equity"] / total_assets * 100