from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse_lazy, reverse


# User_Model = get_user_model()
User_Model = settings.AUTH_USER_MODEL


class ComplaintCategory(models.Model):
    name = models.CharField(max_length=128)
    email_to_send = models.EmailField()
    order = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.name


class Complaint(models.Model):

    STATUS_CHOICES = (("IN", "Inititated"), ("PR", "Processing"), ("SL", "Solved"))

    user = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    category = models.ForeignKey(ComplaintCategory, on_delete=models.CASCADE)
    details = models.TextField(blank=True)

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="IN")

    on = models.DateTimeField(auto_now_add=True)
    processing_on = models.DateTimeField(blank=True, null=True)
    solved_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.get_display_text

    @property
    def get_absolute_url(self):
        return reverse_lazy("complaints:update", kwargs={"pk": self.id})

    @property
    def get_delete_url(self):
        return reverse_lazy("complaints:delete", kwargs={"pk": self.id})

    @property
    def get_status(self):
        return self.get_status_display

    @property
    def get_display_text(self):
        return self.user.get_display_text

