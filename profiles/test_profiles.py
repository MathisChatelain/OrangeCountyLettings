from profiles.models import Profile
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_profiles_index(client):
    """
    Test profiles_index view
    no need to mock since we are using a test readonly database
    """

    response = client.get(reverse("profiles_index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile(client):
    """
    Test profile view
    no need to mock since we are using a test readonly database
    """

    username = Profile.objects.first().user.username
    response = client.get(reverse("profile", args=[username]))
    assert response.status_code == 200
