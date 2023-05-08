from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from SurfWallet.models import SurfBoard, WetSuit, Spot


class SurfBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurfBoard
        fields = '__all__'
        read_only_fields = ('created_at',)


class WetSuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = WetSuit
        fields = '__all__'


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = '__all__'
        extra_kwargs = {
            'fecha': {'read_only': True, 'required': False},
            # 'fecha': {'read_only': True},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'groups', 'email']

        # Hide password
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
