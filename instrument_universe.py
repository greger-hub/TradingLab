from api import _load_instruments


class InstrumentUniverse:
    """
    Provides access to the complete instrument universe
    returned by Börsdata.

    The universe can be filtered by instrument type and country.
    """

    def all(self) -> list[dict]:
        """
        Return all instruments available from Börsdata.
        """
        return list(_load_instruments())

    def filter(
        self,
        country: str | None = None,
        instrument_type: str | None = None,
    ) -> list[dict]:
        """
        Return instruments matching the supplied filters.

        If no filters are provided, all instruments are returned.
        """
        instruments = self.all()

        if country is not None:
            instruments = [
                instrument
                for instrument in instruments
                if instrument.get("country") == country
            ]

        if instrument_type is not None:
            instruments = [
                instrument
                for instrument in instruments
                if instrument.get("instrument") == instrument_type
            ]

        return instruments