from django.db import models

from SurfWallet.choices import SURFBOARD_MATERIALS, FINS_MATERIALS
from SurfWallet.models.user import CustomUser
import os
import base64


def image_as_base64(image_file, format='png'):
    """
    :param `image_file` for the complete path of image.
    :param `format` is format for image, eg: `png` or `jpg`.
    """
    if not os.path.isfile(image_file):
        return None

    encoded_string = ''
    with open(image_file, 'rb') as img_f:
        encoded_string = base64.b64encode(img_f.read())
    return 'data:image/%s;base64,%s' % (format, encoded_string)


class SurfBoard(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='owned_surfboards', on_delete=models.CASCADE)

    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=100, null=True)

    # Board info
    number_of_fins = models.PositiveIntegerField(null=True)

    # Materials
    material = models.PositiveIntegerField(choices=SURFBOARD_MATERIALS, null=True)
    fins_material = models.PositiveIntegerField(choices=FINS_MATERIALS, null=True)

    # Measured in feet (ft)
    length = models.FloatField(null=True)

    # Measured in inches (in)
    width = models.FloatField(null=True)
    thickness = models.FloatField(null=True)

    # Measured in liters (L)
    volume = models.FloatField(null=True)


class SurfboardImage(models.Model):
    surfboard = models.ForeignKey(SurfBoard, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='surfboard_images/')
    is_cover = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.image.name
