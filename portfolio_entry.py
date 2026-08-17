from dataclasses import dataclass

from models import Instrument


@dataclass(frozen=True)
class PortfolioEntry:
    instrument: Instrument
    score: float
