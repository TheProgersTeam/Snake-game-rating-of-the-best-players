from django.db import models
from django.contrib.auth.models import User

class Records(models.Model):
    # Player
    player = models.CharField(max_length=50, null=False, blank=True)
    # Score
    score = models.IntegerField(null=False, blank=True)

    class Meta:
        verbose_name = 'Records'
        verbose_name_plural = 'Records'