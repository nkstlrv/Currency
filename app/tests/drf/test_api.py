from currency.models import Source, Rate


def test_get_api_rates(api_client_auth):
    response = api_client_auth.get("/api/currency/rate/")
    assert response.status_code == 200
    assert response.json()


def test_get_api_rate_valid_id(api_client_auth):
    response = api_client_auth.get("/api/currency/rate/?id=1")
    assert response.status_code == 200
    assert len(response.json()["results"]) == 1


def test_get_api_rate_invalid_id(api_client_auth):
    response = api_client_auth.get("/api/currency/rate/?id=999999")
    assert response.status_code == 200
    assert len(response.json()["results"]) == 0


def test_get_api_rate_invalid_param_format(api_client_auth):
    response = api_client_auth.get("/api/currency/rate/1")
    assert response.status_code == 404


def test_post_empty_api_rates(api_client_auth):
    response = api_client_auth.post("/api/currency/rate/")
    assert response.status_code == 400


def test_post_invalid_data_api_rates(api_client_auth):
    rate_count = Rate.objects.count()
    payload = {"currency": 1, "buy": "INVALID", "sell": "INVALID", "source": 1}
    response = api_client_auth.post("/api/currency/rate/", data=payload)
    assert response.status_code == 400
    assert Rate.objects.count() == rate_count


def test_post_valid_api_rates(api_client_auth):
    rate_count = Rate.objects.count()
    source = Source.objects.create(name="test", dev_name="test")
    payload = {"currency": 2, "buy": "9.99", "sell": "10.10", "source": source.id}
    response = api_client_auth.post("/api/currency/rate/", data=payload)
    assert response.status_code == 201
    assert Rate.objects.count() == rate_count + 1


def test_post_valid_api_rates_no_currency(api_client_auth):
    rate_count = Rate.objects.count()
    source = Source.objects.create(name="test", dev_name="test")
    payload = {"buy": "9.99", "sell": "10.10", "source": source.id}
    response = api_client_auth.post("/api/currency/rate/", data=payload)
    assert response.status_code == 201
    assert Rate.objects.count() == rate_count + 1


def test_rate_destroy_success(api_client_auth):
    rate_count = Rate.objects.count()
    response = api_client_auth.delete("/api/currency/rate/detail-delete/1/")
    assert response.status_code == 204
    assert Rate.objects.count() == rate_count - 1


def test_rate_destroy_fail(api_client_auth):
    rate_count = Rate.objects.count()
    response = api_client_auth.delete("/api/currency/rate/detail-delete/999/")
    assert response.status_code == 404
    assert Rate.objects.count() == rate_count


def test_get_source(api_client_auth):
    response = api_client_auth.get("/api/currency/source/")
    assert response.status_code == 200


def test_get_source_valid_id(api_client_auth):
    response = api_client_auth.get("/api/currency/source/?id=4")
    assert response.status_code == 200
    assert len(response.json()["results"]) == 1


def test_get_source_invalid_id(api_client_auth):
    response = api_client_auth.get("/api/currency/source/?id=9999")
    assert response.status_code == 200
    assert len(response.json()["results"]) == 0


def test_get_source_invalid_query_param(api_client_auth):
    response = api_client_auth.get("/api/currency/source/9999")
    assert response.status_code == 404


def test_post_source_valid(api_client_auth):
    source_count = Source.objects.count()
    payload = {"name": "test", "dev_name": "test", "url": "test"}
    response = api_client_auth.post("/api/currency/source/", data=payload)
    assert response.status_code == 201
    assert response.json()
    assert Source.objects.count() == source_count + 1


def test_post_source_invalid_no_data(api_client_auth):
    source_count = Source.objects.count()
    payload = {}
    response = api_client_auth.post("/api/currency/source/", data=payload)
    assert response.status_code == 400
    assert response.json()
    assert Source.objects.count() == source_count


def test_post_source_invalid_invalid_data(api_client_auth):
    source_count = Source.objects.count()
    payload = {"name": "", "dev_name": "test", "url": "test"}
    response = api_client_auth.post("/api/currency/source/", data=payload)
    assert response.status_code == 400
    assert response.json()
    assert Source.objects.count() == source_count


def test_post_source_invalid_max_length(api_client_auth):
    invalid_url = "".join([str(i) for i in range(300)])
    source_count = Source.objects.count()
    payload = {
        "name": "test",
        "dev_name": "test",
        "url": invalid_url,
    }
    response = api_client_auth.post("/api/currency/source/", data=payload)
    assert response.status_code == 400
    assert response.json()
    assert Source.objects.count() == source_count


def test_source_destroy_success(api_client_auth):
    source_count = Source.objects.count()
    response = api_client_auth.delete("/api/currency/source/detail-delete/4/")
    assert response.status_code == 204
    assert Source.objects.count() == source_count - 1


def test_source_destroy_fail(api_client_auth):
    source_count = Source.objects.count()
    response = api_client_auth.delete("/api/currency/source/detail-delete/999/")
    assert response.status_code == 404
    assert Source.objects.count() == source_count
