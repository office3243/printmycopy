from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Station
from django.contrib.auth.mixins import LoginRequiredMixin
from . import alert_messages


class StationListView(LoginRequiredMixin, ListView):
    model = Station
    template_name = "stations/list.html"
    context_object_name = "stations"
    paginate_by = 10
