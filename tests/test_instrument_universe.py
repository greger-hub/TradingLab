from unittest.mock import Mock

from instrument_universe import InstrumentUniverse
from models import Instrument


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
        Instrument(
            id="4",
            ticker="NOVO B",
            name="Novo Nordisk B",
            country="DK",
            currency="DKK",
        ),
    ]


def make_universe():
    provider = Mock()
    provider.get_instruments.return_value = make_instruments()

    return InstrumentUniverse(provider)


def test_universe_returns_all_instruments():
    universe = make_universe()

    result = universe.all()

    assert len(result) == 4
    assert all(isinstance(instrument, Instrument) for instrument in result)


def test_universe_returns_expected_instruments():
    universe = make_universe()

    result = universe.all()

    assert result[0].ticker == "VOLV B"
    assert result[1].ticker == "INVE B"
    assert result[2].ticker == "ERIC B"
    assert result[3].ticker == "NOVO B"


def test_universe_can_filter_by_country():
    universe = make_universe()

    result = universe.filter(country="SE")

    assert len(result) == 3
    assert all(instrument.country == "SE" for instrument in result)


def test_universe_can_filter_by_denmark():
    universe = make_universe()

    result = universe.filter(country="DK")

    assert len(result) == 1
    assert result[0].ticker == "NOVO B"


def test_universe_returns_empty_when_no_instruments_match():
    universe = make_universe()

    result = universe.filter(country="NO")

    assert result == []


def test_universe_without_filter_returns_all():
    universe = make_universe()

    result = universe.filter()

    assert len(result) == 4


def test_universe_uses_provider():
    provider = Mock()
    provider.get_instruments.return_value = make_instruments()

    universe = InstrumentUniverse(provider)

    universe.all()

    provider.get_instruments.assert_called_once()