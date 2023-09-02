def test_get_api_rates_not_auth(api_client):
    response = api_client.get("/api/currency/rate/")
    assert response.status_code == 401
    assert response.json()


def test_post_empty_api_rates_not_auth(api_client):
    response = api_client.post("/api/currency/rate/")
    assert response.status_code == 401
