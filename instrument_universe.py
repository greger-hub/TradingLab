from data_provider import DataProvider
from models import Instrument


class InstrumentUniverse:
    """
    Provides access to the complete provider-independent
    instrument universe used by TradingLab.

    The universe depends only on the DataProvider contract
    and is therefore independent of the underlying data vendor.
    """

    def __init__(self, provider: DataProvider):
        self._provider = provider

    def all(self) -> list[Instrument]:
        """
        Return all instruments available from the configured provider.
        """
        return list(self._provider.get_instruments())

    def filter(
        self,
        country: str | None = None,
    ) -> list[Instrument]:
        """
        Return instruments matching the supplied country filter.

        If no filter is provided, all instruments are returned.
        """
        instruments = self.all()

        if country is not None:
            instruments = [
                instrument
                for instrument in instruments
                if instrument.country == country
            ]

        return instruments