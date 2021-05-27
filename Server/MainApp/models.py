from django.db import models


class Records(models.Model):
    player = models.CharField(max_length=50, null=False, blank=True)  # Player
    score = models.IntegerField(null=False, blank=True)  # Score

    class Meta:
        verbose_name = 'Records'
        verbose_name_plural = 'Records'
