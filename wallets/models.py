from django.db import models
from django.conf import settings
from django.http import Http404


class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return "{} - {}".format(self.user, self.balance)

    @property
    def get_recharges(self):
        return self.recharge_set.all()

    @property
    def get_success_recharges(self):
        return self.recharge_set.filter(status="SC")

    @property
    def get_failed_recharges(self):
        return self.recharge_set.filter(status="FL")

    @property
    def get_hold_recharges(self):
        return self.recharge_set.filter(status="HD")

    @property
    def get_user(self):
        return self.user

    def deduct_amount(self, amount):
        if not self.balance < amount:
            self.balance -= amount
            self.save()
        else:
            raise Http404("Insufficient Balance")



