from metrics import (

    calculate_operating_margin,

    calculate_debt_ratio,

    calculate_roe,

    calculate_growth,

)

from models import Metrics, AnalysisResult

def score_margin(value):

    if value >= 20:

        return 25, "✅ Mycket hög rörelsemarginal"

    elif value >= 15:

        return 20, "✅ Stark rörelsemarginal"

    elif value >= 10:

        return 15, "🟡 Godkänd rörelsemarginal"

    else:

        return 5, "❌ Låg rörelsemarginal"

def score_debt(value):

    if value < 0.5:

        return 25, "✅ Låg skuldsättning"

    elif value < 1.0:

        return 20, "🟡 Acceptabel skuldsättning"

    else:

        return 10, "❌ Hög skuldsättning"

def score_roe(value):

    if value >= 20:

        return 25, "✅ Mycket hög ROE"

    elif value >= 15:

        return 20, "✅ Stark ROE"

    elif value >= 10:

        return 15, "🟡 Godkänd ROE"

    else:

        return 5, "❌ Låg ROE"

def score_growth(revenue_growth, profit_growth):

    points = 0

    for growth in (revenue_growth, profit_growth):

        if growth >= 15:

            points += 12.5

        elif growth >= 10:

            points += 10

        elif growth >= 5:

            points += 7.5

        elif growth > 0:

            points += 5

    if points >= 20:

        kommentar = "📈 Mycket stark tillväxt"

    elif points >= 10:

        kommentar = "📈 God tillväxt"

    elif points > 0:

        kommentar = "📈 Svag men positiv tillväxt"

    else:

        kommentar = "📉 Ingen eller negativ tillväxt"

    return points, kommentar

def calculate_score(current_report, previous_report):

    kommentarer = []

    operating_margin = calculate_operating_margin(current_report)

    debt_ratio = calculate_debt_ratio(current_report)

    roe = calculate_roe(current_report)

    revenue_growth = calculate_growth(

        current_report,

        previous_report,

        "revenues"

    )

    profit_growth = calculate_growth(

        current_report,

        previous_report,

        "profit_To_Equity_Holders"

    )

    metrics = Metrics(

        operating_margin=operating_margin,

        debt_ratio=debt_ratio,

        roe=roe,

        revenue_growth=revenue_growth,

        profit_growth=profit_growth,

    )

    score = 0

    points, kommentar = score_margin(metrics.operating_margin)

    score += points

    kommentarer.append(kommentar)

    points, kommentar = score_debt(metrics.debt_ratio)

    score += points

    kommentarer.append(kommentar)

    points, kommentar = score_roe(metrics.roe)

    score += points

    kommentarer.append(kommentar)

    points, kommentar = score_growth(

        metrics.revenue_growth,

        metrics.profit_growth,

    )

    score += points

    kommentarer.append(kommentar)

    return AnalysisResult(

        score=score,

        metrics=metrics,

        comments=kommentarer,

    )