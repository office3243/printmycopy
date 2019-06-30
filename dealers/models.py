from django.db import models
from accounts.validators import phone_number_validator
from django.utils.translation import ugettext_lazy as _


class Dealer(models.Model):
    phone = models.CharField(_('phone number'), max_length=13, validators=[phone_number_validator, ], unique=True)
    email = models.EmailField(_('email address'), blank=True)

    first_name = models.CharField(_('first name'), max_length=32, blank=True)
    last_name = models.CharField(_('last name'), max_length=32, blank=True)
    city = models.CharField(_('city'), max_length=30, blank=True, default="Pune")
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    def __str__(self):
        return self.get_display_text

    @property
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def get_display_text(self):
        return self.get_full_name
