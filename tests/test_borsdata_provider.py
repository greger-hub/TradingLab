from unittest.mock import patch

from borsdata_provider import BorsdataProvider
from models import Instrument


def make_borsdata_instruments():
    return [
        {
            "insId": 2,
            "name": "AAK",
            "ticker": "AAK",
            "countryId": 1,
            "stockPriceCurrency": "SEK",
        },
        {
            "insId": 10,
            "name": "Investor B",
            "ticker": "INVE B",
            "countryId": 1,
            "stockPriceCurrency": "SEK",
        },
    ]


def test_provider_returns_tradinglab_instruments():
    with patch(
        "borsdata_provider._load_instruments",
        return_value=make_borsdata_instruments(),
    ):
        provider = BorsdataProvider()

        result = provider.get_instruments()

    assert len(result) == 2
    assert all(isinstance(instrument, Instrument) for instrument in result)


def test_provider_maps_borsdata_fields_to_tradinglab_fields():
    with patch(
        "borsdata_provider._load_instruments",
        return_value=make_borsdata_instruments(),
    ):
        provider = BorsdataProvider()

        result = provider.get_instruments()

    instrument = result[0]

    assert instrument.id == "2"
    assert instrument.ticker == "AAK"
    assert instrument.name == "AAK"
    assert instrument.country == "SE"
    assert instrument.currency == "SEK"


def test_provider_does_not_expose_borsdata_specific_fields():
    with patch(
        "borsdata_provider._load_instruments",
        return_value=make_borsdata_instruments(),
    ):
        provider = BorsdataProvider()

        result = provider.get_instruments()

    instrument = result[0]

    assert not hasattr(instrument, "insId")
    assert not hasattr(instrument, "countryId")
    assert not hasattr(instrument, "stockPriceCurrency")


def test_provider_handles_unknown_country_id():
    data = {
        "insId": 99,
        "name": "Test",
        "ticker": "TEST",
        "countryId": 99,
        "stockPriceCurrency": "EUR",
    }

    instrument = BorsdataProvider._to_instrument(data)

    assert instrument.country == "99"


def test_provider_handles_missing_country_id():
    data = {
        "insId": 100,
        "name": "Test",
        "ticker": "TEST",
        "stockPriceCurrency": "SEK",
    }

    instrument = BorsdataProvider._to_instrument(data)

    assert instrument.country == ""


def test_provider_handles_missing_optional_fields():
    data = {
        "insId": 101,
        "countryId": 1,
    }

    instrument = BorsdataProvider._to_instrument(data)

    assert instrument.id == "101"
    assert instrument.ticker == ""
    assert instrument.name == ""
    assert instrument.country == "SE"
    assert instrument.currency == ""


def test_provider_normalizes_instrument_id_to_string():
    data = {
        "insId": 123,
        "name": "Test",
        "ticker": "TEST",
        "countryId": 1,
        "stockPriceCurrency": "SEK",
    }

    instrument = BorsdataProvider._to_instrument(data)

    assert instrument.id == "123"
    assert isinstance(instrument.id, str)