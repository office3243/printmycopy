from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from .validators import phone_number_validator
from django.conf import settings
import requests
from django.shortcuts import redirect
from django.contrib import messages
from . import alert_messages
from wallets.models import Wallet
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError

api_key_2fa = settings.API_KEY_2FA


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(_('phone number'), max_length=13, validators=[phone_number_validator, ], unique=True)
    email = models.EmailField(_('email address'), blank=True, )

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    phone_verified = models.BooleanField(default=False)
    first_name = models.CharField(_('first name'), max_length=32, blank=True)
    last_name = models.CharField(_('last name'), max_length=32, blank=True)
    city = models.CharField(_('city'), max_length=30, blank=True, default="Pune")
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.phone

    @property
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "{} {}".format(self.first_name, self.last_name)
        return full_name.strip()

    @property
    def get_display_text(self):
        return self.__str__()

    @property
    def get_first_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    @property
    def get_wallet(self):
        return self.wallet

    def make_phone_verified_and_active(self):
        self.is_active = True
        self.phone_verified = True
        self.save()


def create_wallet(instance, sender, *args, **kwargs):
    if not hasattr(instance, 'wallet'):
        Wallet.objects.create(user=instance)


post_save.connect(create_wallet, sender=User)
