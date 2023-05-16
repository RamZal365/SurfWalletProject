
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from SurfWallet.models.user import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'username', 'password', 'groups', 'email', 'birthday',
                  'country', 'city', 'surfing_level']

        # Hide password
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
