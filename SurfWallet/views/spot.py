from rest_framework import viewsets, permissions

from SurfWallet.models.spot import Spot
from SurfWallet.serializers.spot_serializer import SpotSerializer


class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer
    permission_classes = [permissions.AllowAny]
