from collections import OrderedDict

from rest_framework import serializers
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject

from SurfWallet.models.surfboard import SurfboardImage, SurfBoard
from drf_extra_fields.fields import Base64ImageField


class SurfboardImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(represent_in_base64=True)

    class Meta:
        model = SurfboardImage
        fields = ['id', 'image', 'is_cover', 'order']


class SurfBoardSerializer(serializers.ModelSerializer):
    images = SurfboardImageSerializer(many=True, required=False)

    class Meta:
        model = SurfBoard
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images')
        surfboard = SurfBoard.objects.create(**validated_data)
        for image_data in images_data:
            SurfboardImage.objects.create(SurfBoard=surfboard, **image_data)
        return surfboard

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.description = validated_data.get('description', instance.description)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.number_of_fins = validated_data.get('number_of_fins', instance.number_of_fins)
        instance.material = validated_data.get('material', instance.material)
        instance.fins_material = validated_data.get('fins_material', instance.fins_material)
        instance.length = validated_data.get('length', instance.length)
        instance.width = validated_data.get('width', instance.width)
        instance.thickness = validated_data.get('thickness', instance.thickness)
        instance.volume = validated_data.get('volume', instance.volume)

        images_data = validated_data.pop('images')
        SurfboardImage.objects.filter(surfboard=instance).delete()

        for image_data in images_data:
            SurfboardImage.objects.create(surfboard=instance, **image_data)

        instance.save()
        return instance
