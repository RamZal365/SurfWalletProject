from django.contrib.auth.models import User
from django.db import models

from SurfWallet.choices import LEVELS


class CustomUser(User):
    birthday = models.DateField(null=True, blank=True)

    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    started_surfing = models.DateField(null=True, blank=True)
    surfing_level = models.PositiveIntegerField(choices=LEVELS, null=True, blank=True)

    # Measured in kilograms (kg)
    weight = models.FloatField(null=True, blank=True)

    # Measured in feet (ft)
    height = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.get_full_name()

