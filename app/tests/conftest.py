# from django.core.management import call_command
import pytest
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
        user = django_user_model(
            email="test@mail.com",
        )
        user.set_password(password)
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
