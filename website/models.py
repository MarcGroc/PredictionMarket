import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from users.models import UserProfile


class Event(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False)
    category = models.CharField(max_length=20, null=False)
    expiration_date = models.DateField(null=False)
    volume = models.DecimalField(max_digits=20, decimal_places=2, default=1)
    date_created = models.DateField(default=timezone.now)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, related_name='events')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=5) <= self.date_created <= now
