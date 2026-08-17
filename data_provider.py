from typing import Protocol

from models import Instrument


class DataProvider(Protocol):
    """
    Contract for TradingLab data providers.

    Providers must return TradingLab's provider-independent
    Instrument model rather than provider-specific dictionaries.
    """

    def get_instruments(self) -> list[Instrument]:
        """
        Return all available instruments.
        """
        ...
