from django.test import TestCase


def test_root_not_found(client):
    response = client.get('/')

    assert response.status_code == 404

# Create your tests here.
