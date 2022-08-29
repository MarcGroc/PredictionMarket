from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assets = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.user.username}'
