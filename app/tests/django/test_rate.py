from currency.models import Rate


def test_get_index(client):
    response = client.get("/")
    assert (
        response.status_code == 302
    )  # index page is not completed so currently redirecting to Rates List page


def test_get_unknown_page(client):
    response = client.get("/unknown/page")
    assert response.status_code == 404


def test_get_rate_list(client):
    response = client.get("/rates/list/")
    assert response.status_code == 200


def test_create_rate_valid(client):
    payload = {
        "currency": 1,
        "buy": 12.34,
        "sell": 12.34,
        "source": 4,
    }  # id-4 is first pk in test data

    rates_count = Rate.objects.count()
    response = client.post("/rates/create/", data=payload)
    assert response.status_code == 302
    assert response.headers["Location"] == "/rates/list/"
    assert Rate.objects.count() == rates_count + 1


def test_create_rate_no_source(client):
    payload = {
        "currency": 1,
        "buy": 12.34,
        "sell": 12.34,
    }

    rates_count = Rate.objects.count()
    response = client.post("/rates/create/", data=payload)
    assert response.status_code == 200
    assert response.context_data["form"].errors == {
        "source": ["This field is required."],
    }
    assert Rate.objects.count() == rates_count


def test_create_rate_no_currencies(client):
    payload = {"currency": 1, "source": 4}

    rates_count = Rate.objects.count()
    response = client.post("/rates/create/", data=payload)
    assert response.status_code == 200
    assert response.context_data["form"].errors == {
        "buy": ["This field is required."],
        "sell": ["This field is required."],
    }
    assert Rate.objects.count() == rates_count
