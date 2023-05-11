from django.db import models

from SurfWallet.models.user import CustomUser


class Spot(models.Model):
    creator = models.ForeignKey(CustomUser, related_name='created_spots', on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    long_description = models.TextField(null=True)

    # Info of the location of the spot
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
