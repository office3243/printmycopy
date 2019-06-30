from django.db import models
from accounts.validators import phone_number_validator
from .managers import PaymentManager


class Payment(models.Model):

    GATEWAY_CHOICES = (('PAYU', 'Payumoney'), )
    STATUS_CHOICES = (('IN', 'Initiated'), ('SC', 'Success'), ('FL', 'Failed'), ('HD', "Hold"))

    recharge = models.OneToOneField('recharges.Recharge', on_delete=models.CASCADE)

    txnid = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    product_info = models.TextField(blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    gateway = models.CharField(max_length=5, choices=GATEWAY_CHOICES, default='PAYU')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='IN')

    objects = PaymentManager()

    def __str__(self):
        return self.recharge.__str__()

    def verify_payment(self):
        return self.recharge.verify_recharge(amount=self.amount)

    def succeed(self):
        self.status = "SC"
        self.recharge.payment_succeed()
        self.save()

    def failed(self):
        self.status = "FL"
        self.recharge.payment_failed()
        self.save()
