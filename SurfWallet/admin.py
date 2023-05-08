from django.contrib import admin

# Register your models here.
from SurfWallet.models import SurfBoard, WetSuit, Spot

admin.site.register(SurfBoard)
admin.site.register(WetSuit)
admin.site.register(Spot)
