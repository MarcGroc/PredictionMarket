import pytest
from django.contrib.auth.models import User

from users.models import UserProfile


class TestModels:

    @pytest.mark.django_db
    def test_create_profile(self):
        profile = UserProfile.objects.create(id=1, assets=100.00, user_id=3)
        assert profile.assets == 100
        assert profile.user_id == 3
