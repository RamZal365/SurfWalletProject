from django.contrib import admin

# Register your models here.
from SurfWallet.models.spot import Spot
from SurfWallet.models.surfboard import SurfBoard
from SurfWallet.models.user import CustomUser
from SurfWallet.models.wetsuit import WetSuit

admin.site.register(CustomUser)
admin.site.register(SurfBoard)
admin.site.register(WetSuit)
admin.site.register(Spot)
