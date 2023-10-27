import pytest
from django.urls import reverse


@pytest
def test_get_profile_index(client):
    response = client.get(reverse("profiles_index"))
    assert response.status_code == 200
