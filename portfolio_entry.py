from dataclasses import dataclass


@dataclass(frozen=True)
class PortfolioEntry:
    instrument: str
    score: float