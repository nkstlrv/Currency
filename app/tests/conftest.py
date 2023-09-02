# from django.core.management import call_command
import pytest
import os
from dotenv import load_dotenv


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


@pytest.fixture()
def api_client_auth():
    from rest_framework.test import APIClient

    load_dotenv()

    client = APIClient()
    client.login(
        username=os.getenv("TEST_USERNAME"), password=os.getenv("TEST_PASSWORD")
    )
    yield client
