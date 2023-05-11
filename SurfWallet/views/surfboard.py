from rest_framework import viewsets, permissions

from SurfWallet.models.surfboard import SurfBoard
from SurfWallet.serializers.surfboard_serializer import SurfBoardSerializer


class SurfBoardViewSet(viewsets.ModelViewSet):
    queryset = SurfBoard.objects.all()
    serializer_class = SurfBoardSerializer
    permission_classes = [permissions.AllowAny]

