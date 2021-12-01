from django.db import models
from django.utils import timezone

class Challenge(models.Model):
    challengeName = models.CharField(max_length=200, default='')
    challengeDesc = models.TextField()
    release_date = models.DateTimeField(default=timezone.now)