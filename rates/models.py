from django.db import models
from simple_history.models import HistoricalRecords


class Rate(models.Model):
    bw_rate = models.DecimalField(max_digits=4, decimal_places=2)
    color_rate = models.DecimalField(max_digits=4, decimal_places=2)

    history = HistoricalRecords()

    def __str__(self):
        return "bw : {} - color : {}".format(self.bw_rate, self.color_rate)

    @property
    def get_rates_dict(self):
        return {"bw_rate": float(self.bw_rate), "color_rate": float(self.color_rate)}

    @property
    def get_rates_tuple(self):
        return float(self.bw_rate), float(self.color_rate)

    def get_rate(self, color_model):
        return self.bw_rate if color_model == "BW" else self.color_rate