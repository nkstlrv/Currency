from currency.models import ContactUs


def test_get_contactus_list(client):
    response = client.get("/contacts/list/")
    assert response.status_code == 200


def test_post_empty_form_contactus_status(client):
    response = client.post("/contacts/create/")
    assert response.status_code == 200


def test_post_empty_form_contactus_errors(client):
    response = client.post("/contacts/create/")
    assert response.status_code == 200
    assert response.context_data["form"].errors == {
        "email_from": ["This field is required."],
        "subject": ["This field is required."],
        "message": ["This field is required."],
    }


def test_post_invalid_email_contactus_status(client):
    payload = {
        "email_from": "INVALID EMAIL",
        "subject": "Test",
        "message": "Test",
    }
    response = client.post("/contacts/create/", data=payload)
    assert response.status_code == 200


def test_post_invalid_email_contactus_errors(client):
    payload = {
        "email_from": "INVALID EMAIL",
        "subject": "Test",
        "message": "Test",
    }
    response = client.post("/contacts/create/", data=payload)
    # breakpoint()
    assert response.context_data["form"].errors == {
        "email_from": ["Enter a valid email address."],
    }


def test_post_valid_email_contactus(client, mailoutbox):
    db_objects_start = ContactUs.objects.count()
    assert db_objects_start == 0
    payload = {
        "email_from": "VALID_EMAIL@MAIL.COM",
        "subject": "Test",
        "message": "Test",
    }
    response = client.post("/contacts/create/", data=payload)
    db_objects_end = ContactUs.objects.count()
    assert response.status_code == 302
    assert response.headers["Location"] == "/"
    assert len(mailoutbox) == 1
    assert db_objects_end == 1
