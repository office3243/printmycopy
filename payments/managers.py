from django.db import models


class PaymentManager(models.Manager):

    def initiate_payment(self, **kwargs):
        payment = self.create(**kwargs)
        return payment

    def search_payment(self, txnid, amount, wallet_id):
        try:
            payment = self.get_queryset().get(txnid=txnid, amount=amount, recharge__wallet__id=wallet_id)
        except:
            payment = None
        return payment
