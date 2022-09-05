import pytest

from django.urls import reverse


class TestLoginView:
    @pytest.mark.django_db
    def test_strings_should_appear(self, client):
        url = reverse("login")
        response = client.get(url)
        assert response.status_code == 200
        assert b"Log in" in response.content
        assert b"Username" in response.content
        assert b"Password" in response.content
        assert b"Forgot password" in response.content
        assert b"Don't have account?" in response.content


class TestPasswordResetView:
    @pytest.mark.django_db
    def test_strings_should_appear(self, client):
        url = reverse("reset")
        response = client.get(url)
        assert response.status_code == 200
        assert b"Reset Password" in response.content
        assert b"Email" in response.content
        assert b"Reset" in response.content


class TestRegisterView:
    @pytest.mark.django_db
    def test_strings_should_appear(self, client):
        url = reverse("register")
        response = client.get(url)
        assert response.status_code == 200
        assert b"Register account" in response.content
        assert b"Username" in response.content
        assert b"Email" in response.content
        assert b"Password" in response.content
        assert b"Password confirmation" in response.content
        assert b"Already member? Log in" in response.content


class TestProfileView:
    @pytest.mark.django_db
    def test_strings_should_appear(self, client):
        url = reverse("profile")
        response = client.get(url)
        assert response.status_code == 200
