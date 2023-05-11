from django.db import models

from SurfWallet.models.user import CustomUser


class WetSuit(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='owned_wetsuits', on_delete=models.CASCADE)

    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=100, null=True)

    # Measured in feet (ft)
    height = models.FloatField(null=True)

    # Measured in kilograms (kg)
    weight = models.FloatField(null=True)

    # Measured in inches (in)
    chest = models.FloatField(null=True)
    waist = models.FloatField(null=True)

    # Measured in millimeters (mm)
    chest_thickness = models.FloatField(null=True)
    extremities_thickness = models.FloatField(null=True)
