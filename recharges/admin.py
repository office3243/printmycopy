from django.contrib import admin
from . models import Recharge, CustomPack, OfferPack

admin.site.register(Recharge)
admin.site.register(OfferPack)
admin.site.register(CustomPack)

