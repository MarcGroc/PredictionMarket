import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Event(models.Model):
    YES_NO_CHOICE = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    title = models.CharField(max_length=100, unique=True, null=False)
    category = models.CharField(max_length=20, null=False)
    expiration_date = models.DateField(null=False)
    volume = models.DecimalField(max_digits=20, decimal_places=2, default=1)
    date_created = models.DateTimeField(default=timezone.now)
    choice = models.CharField(max_length=3, choices=YES_NO_CHOICE, default='-')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=5) <= self.date_created <= now



