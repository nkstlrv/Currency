from rest_framework.test import APIClient


def test_get_api_rates(api_client):
    response = api_client.get("/api/currency/rate/")
    assert response.status_code == 200
    assert response.json()


def test_post_empty_api_rates(api_client):
    response = api_client.post("/api/currency/rate/")
    assert response.status_code == 400
    # print(response.json())
    assert response.json()["source"] == ["This field is required."]
