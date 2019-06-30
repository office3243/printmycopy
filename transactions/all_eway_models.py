class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(_('phone number'), max_length=13, validators=[phone_number_validator, ], unique=True)
    email = models.EmailField(_('email address'), blank=True)

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    phone_verified = models.BooleanField(default=False)
    first_name = models.CharField(_('first name'), max_length=32, blank=True)
    last_name = models.CharField(_('last name'), max_length=32, blank=True)
    city = models.CharField(_('city'), max_length=30, blank=True, default="Pune")
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)



class Dealer(models.Model):
    phone = models.CharField(_('phone number'), max_length=13, validators=[phone_number_validator, ], unique=True)
    email = models.EmailField(_('email address'), blank=True)

    first_name = models.CharField(_('first name'), max_length=32, blank=True)
    last_name = models.CharField(_('last name'), max_length=32, blank=True)
    city = models.CharField(_('city'), max_length=30, blank=True, default="Pune")
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)



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



class Rate(models.Model):
    bw_rate = models.PositiveSmallIntegerField(default=1)
    color_rate = models.PositiveSmallIntegerField(default=1)

    class OfferPack(models.Model):
        name = models.CharField(max_length=16)
        headline = models.CharField(max_length=48)
        price = models.DecimalField(max_digits=6, decimal_places=2)
        balance = models.DecimalField(max_digits=6, decimal_places=2)
        details = models.TextField(blank=True)
        active = models.BooleanField(default=True)
        preference = models.PositiveSmallIntegerField(default=1)



class CustomPack(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    balance = models.DecimalField(decimal_places=2, max_digits=6)



class Recharge(models.Model):

    STATUS_CHOICES = (('IN', 'Initiated'), ('SC', 'Success'), ('FL', 'Failed'), ('HD', "Hold"))

    # user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)

    pack_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    pack_id = models.PositiveIntegerField()
    pack = GenericForeignKey('pack_type', 'pack_id')

    created_on = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='IN')

class StationClass(models.Model):
    name = models.CharField(max_length=32)
    color_name = models.CharField(max_length=32, blank=True)
    color_hex_code = models.CharField(max_length=7, blank=True)




class Station(models.Model):

    dealer = models.ForeignKey("dealers.Dealer", on_delete=models.PROTECT)
    station_class = models.ForeignKey(StationClass, on_delete=models.CASCADE)

    name = models.CharField(max_length=32)
    code = models.CharField(max_length=6, unique=True)
    water_mark = models.FileField(upload_to='station/water_marks/', null=True, blank=True)
    coordinates = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    locality = models.CharField(max_length=32, blank=True)
    city = models.CharField(max_length=32, blank=True)
    embed_code = models.TextField(blank=True)
    details = models.TextField(blank=True)




class Transaction(models.Model):
    PAYMENT_MODE_CHOICES = (('AC', "Account"), ('CO', "Coin"))
    COLOR_MODEL_CHOICES = (('BW', 'Black&White'), ('CL', 'Colorful'))
    PAPER_TYPE_CHOICES = (('NM', 'Normal'), ('LT', 'Letter'), ('PP', "Photo Paper"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    file = models.FileField(upload_to="transactions/transaction_files/{}/".format(datetime.date.today()))
    otp_1 = models.CharField(max_length=4)
    otp_2 = models.CharField(max_length=4)
    amount = models.DecimalField(decimal_places=2, max_digits=5)
    payment_mode = models.CharField(max_length=2, choices=PAYMENT_MODE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    color_model = models.CharField(max_length=2, default='BW', choices=COLOR_MODEL_CHOICES)
    copies = models.PositiveSmallIntegerField(default=1)
    paper_type = models.CharField(max_length=2, default='NM', choices=PAPER_TYPE_CHOICES)

    printed = models.BooleanField(default=False)
    printed_on = models.DateTimeField(blank=True, null=True)
    printed_station = models.ForeignKey('stations.Station', on_delete=models.PROTECT, blank=True, null=True)

    details = models.TextField(blank=True)



class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)