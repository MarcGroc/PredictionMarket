from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    assets = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    choice = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'
