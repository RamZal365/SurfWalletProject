from rest_framework import serializers

from SurfWallet.models.surfboard import SurfboardImage, SurfBoard


class SurfboardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurfboardImage
        fields = ['id', 'image', 'is_cover', 'order']


class SurfBoardSerializer(serializers.ModelSerializer):
    images = SurfboardImageSerializer(many=True, required=False)

    class Meta:
        model = SurfBoard
        fields = '__all__'
        read_only_fields = ('created_at',)
