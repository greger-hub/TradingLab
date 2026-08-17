from models import Instrument


def test_instrument_contains_provider_independent_fields():
    instrument = Instrument(
        id="SE0011337708",
        ticker="AAK",
        name="AAK",
        country="SE",
        currency="SEK",
    )

    assert instrument.id == "SE0011337708"
    assert instrument.ticker == "AAK"
    assert instrument.name == "AAK"
    assert instrument.country == "SE"
    assert instrument.currency == "SEK"


def test_instrument_is_immutable():
    instrument = Instrument(
        id="SE0011337708",
        ticker="AAK",
        name="AAK",
        country="SE",
        currency="SEK",
    )

    try:
        instrument.name = "Something Else"
    except Exception:
        pass
    else:
        raise AssertionError("Instrument should be immutable")


def test_instrument_has_no_provider_specific_fields():
    instrument = Instrument(
        id="SE0011337708",
        ticker="AAK",
        name="AAK",
        country="SE",
        currency="SEK",
    )

    assert not hasattr(instrument, "insId")
    assert not hasattr(instrument, "countryId")
    assert not hasattr(instrument, "marketId")