# from django.core.management import call_command
import pytest
from django.core.management import call_command
from rest_framework.test import APIClient


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture()
def api_client():
    from rest_framework.test import APIClient

    client = APIClient()
    yield client


@pytest.fixture(scope="function")
def api_client_auth(django_user_model):
    client = APIClient()
    password = "test"

    try:
        user = django_user_model.objects.get(email="test@mail.com")
    except django_user_model.DoesNotExist:
        user = django_user_model.objects.create(
            email="test@mail.com",
        )
        user.set_password(password)
        user.is_active = True
        user.save()

    token_response = client.post(
        "/api/auth/token/",
        data={"email": user.email, "password": password},
    )

    assert token_response.status_code == 200
    access = token_response.json().get("access")
    client.credentials(HTTP_AUTHORIZATION=f"JWT {access}")

    yield client

    user.delete()


@pytest.fixture(scope="session", autouse=True)
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        fixtures = ("sources.json", "rates.json", "contact_us.json")
        for fixture in fixtures:
            call_command("loaddata", f"app/tests/fixtures/{fixture}")
