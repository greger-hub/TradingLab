from models import Instrument
from instrument_universe import InstrumentUniverse


class FakeProvider:
    def __init__(self, instruments: list[Instrument]):
        self._instruments = instruments

    def get_instruments(self) -> list[Instrument]:
        return list(self._instruments)


def make_instruments():
    return [
        Instrument(
            id="1",
            ticker="VOLV B",
            name="Volvo B",
            country="SE",
            currency="SEK",
        ),
        Instrument(
            id="2",
            ticker="INVE B",
            name="Investor B",
            country="SE",
            currency="SEK",
        ),
        Instrument(
            id="3",
            ticker="ERIC B",
            name="Ericsson B",
            country="SE",
            currency="SEK",
        ),
    ]


def test_universe_returns_all_instruments():
    provider = FakeProvider(make_instruments())
    universe = InstrumentUniverse(provider)

    result = universe.all()

    assert len(result) == 3
    assert result[0].name == "Volvo B"
    assert result[1].name == "Investor B"
    assert result[2].name == "Ericsson B"


def test_universe_can_filter_by_country():
    instruments = make_instruments()

    instruments.append(
        Instrument(
            id="4",
            ticker="NOVO B",
            name="Novo Nordisk B",
            country="DK",
            currency="DKK",
        )
    )

    provider = FakeProvider(instruments)
    universe = InstrumentUniverse(provider)

    result = universe.filter(country="SE")

    assert len(result) == 3
    assert all(
        instrument.country == "SE"
        for instrument in result
    )


def test_universe_can_return_all_without_filter():
    provider = FakeProvider(make_instruments())
    universe = InstrumentUniverse(provider)

    result = universe.filter()

    assert len(result) == 3


def test_universe_returns_empty_when_no_instruments_match():
    provider = FakeProvider(make_instruments())
    universe = InstrumentUniverse(provider)

    result = universe.filter(country="NO")

    assert result == []


def test_universe_returns_instrument_objects():
    provider = FakeProvider(make_instruments())
    universe = InstrumentUniverse(provider)

    result = universe.all()

    assert all(
        isinstance(instrument, Instrument)
        for instrument in result
    )