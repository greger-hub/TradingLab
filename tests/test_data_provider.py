from data_provider import DataProvider
from models import Instrument


def test_data_provider_contract():
    class FakeProvider:
        def get_instruments(self) -> list[Instrument]:
            return [
                Instrument(
                    id="test-1",
                    ticker="TEST",
                    name="Test Instrument",
                    country="Sweden",
                    currency="SEK",
                )
            ]

    provider: DataProvider = FakeProvider()

    instruments = provider.get_instruments()

    assert len(instruments) == 1
    assert instruments[0].ticker == "TEST"