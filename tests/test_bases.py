from django.urls import reverse


def test_get_home_page(client):
    response = client.get(reverse("index"))
    assert response.status_code == 200
