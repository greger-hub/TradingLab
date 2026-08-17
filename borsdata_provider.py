from api import _load_instruments
from models import Instrument


_COUNTRY_MAP = {
    1: "SE",
    2: "FI",
    3: "NO",
    4: "DK",
}


class BorsdataProvider:
    """
    Adapter between Börsdata and TradingLab's internal data model.

    Börsdata-specific fields are translated here and should not
    leak into the rest of TradingLab.
    """

    def get_instruments(self) -> list[Instrument]:
        """
        Return Börsdata instruments as TradingLab Instruments.
        """
        instruments = _load_instruments()

        return [
            self._to_instrument(instrument)
            for instrument in instruments
        ]

    @staticmethod
    def _to_instrument(data: dict) -> Instrument:
        """
        Convert one Börsdata instrument to a TradingLab Instrument.
        """
        country_id = data.get("countryId")

        country = _COUNTRY_MAP.get(
            country_id,
            str(country_id) if country_id is not None else "",
        )

        return Instrument(
            id=str(data["insId"]),
            ticker=data.get("ticker", ""),
            name=data.get("name", ""),
            country=country,
            currency=data.get("stockPriceCurrency", ""),
        )
