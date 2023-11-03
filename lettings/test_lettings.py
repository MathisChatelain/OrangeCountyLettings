from lettings.models import Letting, Address
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_lettings_index(client):
    response = client.get(reverse("lettings_index"))
    assert response.status_code == 200
