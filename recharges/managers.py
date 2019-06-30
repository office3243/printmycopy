from django.db import models
from payments import views as payment_views


class OfferPackManager(models.Manager):
    def get_offer_packs(self):
        return self.get_queryset().filter(is_active=True).order_by('preference')


class RechargeManager(models.Manager):

    def initiate_recharge(self, **kwargs):
        recharge = self.create(**kwargs)
        payment_views.create_payment(recharge)
