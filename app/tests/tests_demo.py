def test_index(client):
    response = client.get("/")
    assert (
        response.status_code == 302
    )  # index page is not completed so currently redirecting to Rates List page
