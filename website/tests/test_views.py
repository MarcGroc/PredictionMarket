import pytest
from django.test import Client

from django.urls import reverse

c = Client()


class TestHomeView:

    @pytest.mark.django_db
    def test_strings_should_appear(self, client):
        url = reverse('home')
        response = client.get(url)
        assert response.status_code == 200
        assert b'All Events' in response.content
        assert b'Sports' in response.content
        assert b'Economics' in response.content
        assert b'Politics' in response.content
        assert b'New' in response.content
        assert b'Other' in response.content
        assert b'Search' in response.content


class TestSportsView:
    @pytest.mark.django_db
    def test_strings_should_appear(self, client):
        url = reverse('sports')
        response = client.get(url)
        assert response.status_code == 200


class TestEconomicsView:
    @pytest.mark.django_db
    def test_strings_should_appear(self, client):
        url = reverse('economics')
        response = client.get(url)
        assert response.status_code == 200


class TestPoliticsView:
    @pytest.mark.django_db
    def test_strings_should_appear(self, client):
        url = reverse('politics')
        response = client.get(url)
        assert response.status_code == 200


class TestNewView:
    @pytest.mark.django_db
    def test_strings_should_appear(self, client):
        url = reverse('new')
        response = client.get(url)
        assert response.status_code == 200


class TestOtherView:
    @pytest.mark.django_db
    def test_strings_should_appear(self, client):
        url = reverse('other')
        response = client.get(url)
        assert response.status_code == 200


class TestEventView:
    @pytest.mark.django_db
    def test_strings_should_appear(self, client):
        url = reverse(f'event/{1}')
        response = client.get(url)
        assert response.status_code == 200