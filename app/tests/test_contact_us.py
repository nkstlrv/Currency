def test_get_contactus_list(client):
    response = client.get("/contacts/list/")
    assert response.status_code == 200


def test_post_empty_form_contactus(client):
    response = client.post("/contacts/create/")
    assert response.status_code == 200
    assert response.context_data["form"].errors == {
        "email_from": ["This field is required."],
        "subject": ["This field is required."],
        "message": ["This field is required."],
    }
