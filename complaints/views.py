from django.shortcuts import render, redirect, get_object_or_404
from .forms import ComplaintAddForm, ComplaintUpdateForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Complaint
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages
from . import alert_messages


class ComplaintListView(LoginRequiredMixin, ListView):
    model = Complaint
    template_name = "complaints/list.html"
    context_object_name = "complaints"

    def get_queryset(self):
        return self.request.user.complaint_set.all()


class ComplaintAddView(LoginRequiredMixin, CreateView):
    template_name = "complaints/add.html"
    form_class = ComplaintAddForm
    model = Complaint
    success_url = reverse_lazy('complaints:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, alert_messages.COMPLAINT_ADDED_MESSGAE)
        return super().form_valid(form)


class ComplaintUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "complaints/update.html"
    form_class = ComplaintUpdateForm
    model = Complaint
    success_url = reverse_lazy('complaints:list')
    context_object_name = "complaint"

    def get_object(self, queryset=None):
        complaint = super().get_object()
        if complaint.user == self.request.user:
            return complaint
        else:
            raise Http404("No Complaint Found")

    def form_valid(self, form):
        messages.success(self.request, alert_messages.COMPLAINT_UPDATED_MESSGAE)
        return super().form_valid(form)


class ComplaintDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "complaints/delete.html"
    model = Complaint
    success_url = reverse_lazy('complaints:list')
    context_object_name = "complaint"

    def get_object(self, queryset=None):
        complaint = super().get_object()
        if complaint.user == self.request.user:
            return complaint
        else:
            raise Http404("No Complaint Found")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, alert_messages.COMPLAINT_DELETED_MESSGAE)
        return super().delete(request, *args, **kwargs)
