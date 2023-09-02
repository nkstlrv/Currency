def test_get_index(client):
    response = client.get("/")
    assert (
        response.status_code == 302
    )  # index page is not completed so currently redirecting to Rates List page


def test_get_rate_list(client):
    response = client.get("/rates/list/")
    assert response.status_code == 200


def test_get_contactus_list(client):
    response = client.get("/contacts/list/")
    assert response.status_code == 200


def test_get_source_list(client):
    response = client.get("/sources/list/")
    assert response.status_code == 200


def test_get_middleware_logs_list(client):
    response = client.get("/requestresponcelogs/list/")
    assert response.status_code == 200
