import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_guest_user(client):
    create_url = reverse("api-v1-users:guest-create-guest-user")
    create_response = client.post(create_url)
    verify_url = reverse("jwt-verify")
    verify_response = client.post(verify_url, data={"token": create_response.data["access"]})
    assert verify_response.status_code == 200
