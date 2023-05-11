from django.contrib.auth.models import User
from django.db import models

from SurfWallet.choices import LEVELS


class CustomUser(User):
    birthday = models.DateField()

    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    started_surfing = models.DateField(null=True)
    surfing_level = models.PositiveIntegerField(choices=LEVELS)

    # Measured in kilograms (kg)
    weight = models.FloatField(null=True)

    # Measured in feet (ft)
    height = models.FloatField(null=True)

    def __str__(self):
        return self.get_full_name()

