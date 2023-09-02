from unittest.mock import MagicMock

from currency import consts
from currency.choices import RateCurrencyChoices
from currency.models import Rate, Source
from currency.tasks import get_currency_privatbank

privatbank_test_data = [
    {"ccy": "EUR", "base_ccy": "UAH", "buy": "1", "sale": "2"},
    {"ccy": "USD", "base_ccy": "UAH", "buy": "3", "sale": "4"},
    {"ccy": "PLN", "base_ccy": "UAH", "buy": "5", "sale": "6"},
]


def test_privatbank_parser(mocker):
    request_get_mock = mocker.patch(
        "requests.get", return_value=MagicMock(json=lambda: privatbank_test_data)
    )

    rate_count = Rate.objects.count()

    get_currency_privatbank()

    new_rate_count = rate_count + 2
    assert Rate.objects.count() == new_rate_count
    assert request_get_mock.call_count == 1
    assert (
        request_get_mock.call_args[0][0]
        == "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )


def test_privatbank_parser_prevent_duplicates(mocker):
    request_get_mock = mocker.patch(
        "requests.get", return_value=MagicMock(json=lambda: privatbank_test_data)
    )
    source = Source.objects.get(dev_name=consts.PRIVATBANK_DEV_NAME)
    Rate.objects.create(
        buy="39.62", sell="39.62", source=source, currency=RateCurrencyChoices.EUR
    )
    Rate.objects.create(
        buy="36.56", sell="37.45", source=source, currency=RateCurrencyChoices.USD
    )

    rate_count = Rate.objects.count()

    get_currency_privatbank()

    assert Rate.objects.count() == rate_count
    assert request_get_mock.call_count == 1
