import pytest

from website.models import Event

from django.contrib.auth.models import User


class TestModels:

    @pytest.mark.django_db
    def test_user_create(self):
        user = User.objects.create_user('test', 'test@test.com', 'test')
        assert User.objects.count() == 1
        assert user.username == 'test'
        assert user.email == 'test@test.com'
        assert len(user.password) > 0
        assert user.is_superuser is False

    @pytest.mark.django_db
    def test_event_create(self):
        event = Event.objects.create(title='test', category='other', expiration_date='2022-09-30', volume='1.00')
        assert event.title == 'test'
        assert event.category == 'other'
        assert event.expiration_date == '2022-09-30'
        assert event.volume == '1.00'
