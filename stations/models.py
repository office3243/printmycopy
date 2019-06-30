from django.db import models


class StationClass(models.Model):
    rate = models.ForeignKey('rates.Rate', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    color_name = models.CharField(max_length=32, blank=True)
    color_hex_code = models.CharField(max_length=7, blank=True)
    details = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


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
    link = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def get_link(self):
        if self.link:
            return self.link
        else:
            return "-"
