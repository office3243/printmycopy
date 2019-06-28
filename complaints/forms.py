from django import forms
from django.contrib.auth import get_user_model
from .models import Complaint


class ComplaintAddForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ('category', 'details')


class ComplaintUpdateForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ('category', 'details')
