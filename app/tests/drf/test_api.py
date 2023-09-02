from currency.models import Source


def test_get_api_rates(api_client):
    response = api_client.get("/api/currency/rate/")
    assert response.status_code == 200
    assert response.json()


def test_post_empty_api_rates(api_client):
    response = api_client.post("/api/currency/rate/")
    assert response.status_code == 400


def test_post_valid_api_rates(api_client):
    source = Source.objects.create(name="test", dev_name="test")
    payload = {"buy": "9.99", "sell": "10.10", "source": source.id}
    response = api_client.post("/api/currency/rate/", data=payload)
    assert response.status_code == 201
