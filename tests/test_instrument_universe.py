from unittest.mock import patch

from instrument_universe import InstrumentUniverse


def make_instruments():
    return [
        {
            "insId": 1,
            "ticker": "VOLV B",
            "name": "Volvo B",
            "country": "Sweden",
            "instrument": "Stock",
        },
        {
            "insId": 2,
            "ticker": "INVE B",
            "name": "Investor B",
            "country": "Sweden",
            "instrument": "Stock",
        },
        {
            "insId": 3,
            "ticker": "ERIC B",
            "name": "Ericsson B",
            "country": "Sweden",
            "instrument": "Stock",
        },
    ]


def test_universe_returns_all_instruments():
    with patch(
        "instrument_universe._load_instruments",
        return_value=make_instruments(),
    ):
        universe = InstrumentUniverse()

        result = universe.all()

    assert len(result) == 3
    assert result[0]["name"] == "Volvo B"
    assert result[1]["name"] == "Investor B"
    assert result[2]["name"] == "Ericsson B"


def test_universe_can_filter_stocks():
    with patch(
        "instrument_universe._load_instruments",
        return_value=make_instruments(),
    ):
        universe = InstrumentUniverse()

        result = universe.filter(instrument_type="Stock")

    assert len(result) == 3


def test_universe_can_filter_by_country():
    instruments = make_instruments()

    instruments.append(
        {
            "insId": 4,
            "ticker": "NOVO B",
            "name": "Novo Nordisk B",
            "country": "Denmark",
            "instrument": "Stock",
        }
    )

    with patch(
        "instrument_universe._load_instruments",
        return_value=instruments,
    ):
        universe = InstrumentUniverse()

        result = universe.filter(country="Sweden")

    assert len(result) == 3
    assert all(
        instrument["country"] == "Sweden"
        for instrument in result
    )


def test_universe_can_filter_by_country_and_type():
    instruments = make_instruments()

    instruments.append(
        {
            "insId": 4,
            "ticker": "TEST",
            "name": "Test Fund",
            "country": "Sweden",
            "instrument": "Fund",
        }
    )

    with patch(
        "instrument_universe._load_instruments",
        return_value=instruments,
    ):
        universe = InstrumentUniverse()

        result = universe.filter(
            country="Sweden",
            instrument_type="Stock",
        )

    assert len(result) == 3


def test_universe_returns_empty_when_no_instruments_match():
    with patch(
        "instrument_universe._load_instruments",
        return_value=make_instruments(),
    ):
        universe = InstrumentUniverse()

        result = universe.filter(country="Norway")

    assert result == []
