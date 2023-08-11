from celery import shared_task
import time
from django.core.mail import send_mail
import logging
import requests
from currency.consts import PRIVATBANK_DEV_NAME, MONOBANK_DEV_NAME
from currency.choices import RateCurrencyChoices
from currency.utils import to_2_places_decimal

logging.basicConfig(level=logging.INFO, format="%(message)s")


@shared_task
def debug_task():
    for i in range(10):
        logging.info(f"TESTING WORKER")
        time.sleep(0.3)
    return True


@shared_task
def send_email_contact_us(cleaned_data: dict):
    email_body = f"""
            From: {cleaned_data['email_from']}
            Subject: {cleaned_data['subject']}
            Message: {cleaned_data['message']}
            """

    from django.conf import settings

    send_mail(
        "Contact Us",
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )
    return True


@shared_task
def send_signup_verify_email(subject, body, from_email, recipient: str):
    send_mail(
        subject,
        body,
        from_email,
        [recipient],
        fail_silently=False,
    )


@shared_task
def get_currency_privatbank():
    logging.info("PARSING PRIVATBANK")
    from currency.models import Rate, Source

    privatbank_api_url = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"

    source = Source.objects.filter(dev_name=PRIVATBANK_DEV_NAME).first()
    if source is None:
        Source.objects.create(
            dev_name=PRIVATBANK_DEV_NAME, name="PrivatBank", url=privatbank_api_url
        )
        logging.info("NEW PRIVATBANK SOURCE")

    response = requests.get(privatbank_api_url)
    response.raise_for_status()

    rates = response.json()

    available_currencies = {
        "USD": RateCurrencyChoices.USD,
        "EUR": RateCurrencyChoices.EUR,
    }

    for rate in rates:
        currency = rate["ccy"]
        buy = to_2_places_decimal(rate["buy"])
        sell = to_2_places_decimal(rate["sale"])

        if currency not in available_currencies.keys():
            continue

        last_rate = (
            Rate.objects.filter(source=source, currency=available_currencies[currency])
            .order_by("-created")
            .first()
        )

        if last_rate is None or last_rate.buy != buy or last_rate.sell != sell:
            Rate.objects.create(
                currency=available_currencies[currency],
                buy=buy,
                sell=sell,
                source=source,
            )
            logging.info("NEW PRIVATBANK RATE")


@shared_task
def get_currency_monobank():
    logging.info("PARSING MONOBANK")
    from currency.models import Rate, Source

    monobank_api_url = "https://api.monobank.ua/bank/currency"

    source = Source.objects.filter(dev_name=MONOBANK_DEV_NAME).first()
    if source is None:
        Source.objects.create(
            dev_name=MONOBANK_DEV_NAME, name="MonoBank", url=monobank_api_url
        )
        logging.info("NEW MONOBANK SOURCE")

    response = requests.get(monobank_api_url)
    response.raise_for_status()

    rates = response.json()[0:2]  # only us dollar and euro have buy/sell

    available_currencies = {
        840: RateCurrencyChoices.USD,
        978: RateCurrencyChoices.EUR,
    }

    for rate in rates:
        currency = rate["currencyCodeA"]
        buy = to_2_places_decimal(rate["rateBuy"])
        sell = to_2_places_decimal(rate["rateSell"])

        if currency not in available_currencies.keys():
            continue

        last_rate = (
            Rate.objects.filter(source=source, currency=available_currencies[currency])
            .order_by("-created")
            .first()
        )

        if last_rate is None or last_rate.buy != buy or last_rate.sell != sell:
            Rate.objects.create(
                currency=available_currencies[currency],
                buy=buy,
                sell=sell,
                source=source,
            )
            logging.info("NEW MONOBANK RATE")


def mono_api():
    return requests.get("https://api.monobank.ua/bank/currency").json()


if __name__ == "__main__":
    print(mono_api()[0:2])
    ...
