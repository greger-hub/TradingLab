from portfolio_strategies.quality_portfolio_strategy import (
    QualityPortfolioStrategy,
)

from screener import Screener


tickers = [
    "INVE-B.ST",
    "VOLV-B.ST",
    "ERIC-B.ST",
    "HM-B.ST",
]

screener = Screener()
screener.analyze(tickers)
print(f"Antal resultat: {len(screener.results)}")
print("\nQuality scores:\n")

for result in screener.results:
    print(
        result.instrument.name,
        result.quality.score,
    )

strategy = QualityPortfolioStrategy()

portfolio = strategy.build(
    screener,
    size=3,
)

print()
print(strategy.name)
print(strategy.description)
print()

for entry in portfolio.entries:
    print(entry)