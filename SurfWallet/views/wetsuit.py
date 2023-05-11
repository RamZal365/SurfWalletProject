from rest_framework import viewsets, permissions

from SurfWallet.models.wetsuit import WetSuit
from SurfWallet.serializers.wetsuit_serializer import WetSuitSerializer


class WetSuitViewSet(viewsets.ModelViewSet):
    queryset = WetSuit.objects.all()
    serializer_class = WetSuitSerializer
    permission_classes = [permissions.AllowAny]
