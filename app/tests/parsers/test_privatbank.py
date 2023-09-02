from unittest.mock import MagicMock

from currency import consts
from currency.choices import RateCurrencyChoices
from currency.models import Rate, Source
from currency.tasks import get_currency_privatbank

privatbank_test_data = [
    {"ccy": "EUR", "base_ccy": "UAH", "buy": "39.43920", "sale": "42.01681"},
    {"ccy": "USD", "base_ccy": "UAH", "buy": "36.56860", "sale": "37.45318"},
    {"ccy": "PLN", "base_ccy": "UAH", "buy": "36.56860", "sale": "37.45318"},
]


def test_privatbank_parser(mocker):
    request_get_mock = mocker.patch(
        "requests.get", return_value=MagicMock(json=lambda: privatbank_test_data)
    )

    db_objects_count_before_test = Rate.objects.count()

    get_currency_privatbank()

    assert Rate.objects.count() == db_objects_count_before_test + 2
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
        buy="39.43", sell="42.01", source=source, currency=RateCurrencyChoices.EUR
    )
    Rate.objects.create(
        buy="36.56", sell="37.45", source=source, currency=RateCurrencyChoices.USD
    )

    db_objects_count_before_test = Rate.objects.count()

    get_currency_privatbank()

    assert Rate.objects.count() == db_objects_count_before_test
    assert request_get_mock.call_count == 1
