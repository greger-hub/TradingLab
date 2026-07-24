from screener import Screener
from portfolio_builder import PortfolioBuilder


tickers = [
    "Investor",
    "Volvo",
    "Atlas Copco",
]

screener = Screener()
screener.analyze(tickers)

builder = PortfolioBuilder(
    screener.ranking_manager
)

portfolio = builder.build(
    ranking="total",
    size=2,
)

print("\nPORTFOLIO\n")

for entry in portfolio.entries:
    print(entry)