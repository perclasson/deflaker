import pytest
from .currency import Currency


class TestCurrency:

    def test_format_value_in_usd(self):
        assert Currency(5, 'USD').format_value() == '$5'


    def test_format_value_in_eur(self):
        assert Currency(5, 'EUR').format_value() == '5€'

    def test_format_value_in_sek(self):
        with pytest.raises(NotImplementedError):
            Currency(1, 'SEK').format_value()

    def test_with_date(self):
        assert Currency(1, 'USD') == '5$ on 2019-01-26'