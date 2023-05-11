from rest_framework import serializers

from SurfWallet.models.wetsuit import WetSuit


class WetSuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WetSuit
        fields = '__all__'
