from screener import Screener

tickers = [
    "Investor",
    "Volvo",
    "Atlas Copco",
]

screener = Screener()

screener.analyze(tickers)

print(f"\nAnalyserade bolag: {len(screener.results)}")

print("\nTOTAL RANKING\n")

for entry in screener.ranking_manager.get("total").top():
    print(entry)