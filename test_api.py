from api import get_instrument

for ticker in [
    "INVE-B.ST",
    "INVE-B",
    "INVE B",
    "VOLV-B.ST",
    "VOLV-B",
    "VOLV B",
]:
    print(ticker, "->", get_instrument(ticker))