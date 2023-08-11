from celery import shared_task
import time
from django.core.mail import send_mail
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


@shared_task
def demo_task():
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
