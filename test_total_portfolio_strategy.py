from screener import Screener

from portfolio_strategies.total_portfolio_strategy import (
    TotalPortfolioStrategy,
)

tickers = [
    "Investor",
    "Volvo",
    "Atlas Copco",
]

screener = Screener()
screener.analyze(tickers)

strategy = TotalPortfolioStrategy()

portfolio = strategy.build(
    screener,
    size=2,
)

print(strategy.name)
print(strategy.description)

print()

for entry in portfolio.entries:
    print(entry)