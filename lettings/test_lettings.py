import pytest
from django.urls import reverse

from lettings.models import Letting


@pytest.mark.django_db
def test_lettings_index(client):
    """
    Test lettings_index view
    no need to mock since we are using a test readonly database
    """

    response = client.get(reverse("lettings_index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting(client):
    """
    Test letting view
    no need to mock since we are using a test readonly database
    """

    letting = Letting.objects.first()
    response = client.get(reverse("letting", args=[letting.id]))
    assert response.status_code == 200
