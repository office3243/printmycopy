import requests
from .forms import RegisterForm, PasswordResetForm, PasswordResetNewForm, OTPForm, ProfileUpdateForm
from django.views.generic import TemplateView, ListView, FormView, View, DetailView, UpdateView
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import alert_messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from accounts.models import User


USER_MODEL = User
api_key = settings.API_KEY_2FA


def check_otp_2fa(otp, otp_session_data):
    url = "http://2factor.in/API/V1/{0}/SMS/VERIFY/{1}/{2}".format(api_key,
                                                                   otp_session_data, otp)
    response = requests.request("GET", url)
    data = response.json()
    return data['Status'] == "Success"


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "accounts/register.html"

    def form_valid(self, form):
        new_user = form.save()
        return new_user.otp_generate(self.request)


def otp_resend(request):
    try:
        user = USER_MODEL.objects.get(uuid=request.session.get("user_session_uuid"))
        return user.otp_generate(request)
    except USER_MODEL.DoesNotExist:
        raise Http404("Bad Request")


def password_reset_otp_resend(request):
    try:
        user = USER_MODEL.objects.get(uuid=request.session.get("user_session_uuid"))
        return user.password_reset_otp_generate(request)
    except USER_MODEL.DoesNotExist:
        raise Http404("Bad Request")


class OTPVerifyView(FormView):

    form_class = OTPForm
    template_name = "accounts/otp_verify.html"

    def post(self, request, *args, **kwargs):
        otp = request.POST['otp']
        user = USER_MODEL.objects.get(uuid=request.session["user_session_uuid"])
        otp_match = check_otp_2fa(otp=otp, otp_session_data=request.session['user_session_data'])
        if otp_match:
            user.make_phone_verified_and_active()
            del request.session['user_session_uuid']
            del request.session['user_session_data']
            messages.success(request, alert_messages.REGISTERATION_SUCCESS_MESSAGE)
            login(request, user)
            return redirect("portal:home")
        else:
            messages.warning(request, alert_messages.OTP_INCORRECT_MESSAGE)
            return redirect("accounts:otp_verify")


@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, alert_messages.PASSWORD_CHANGED_SUCCESS_MESSAGE)
            return redirect('portal:home')
        else:
            messages.error(request, alert_messages.FORM_INVALID_MESSAGE)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form
    })


class PasswordResetView(FormView):

    template_name = "accounts/password_reset.html"
    form_class = PasswordResetForm

    def form_valid(self, form):
        phone = form.cleaned_data.get('phone')
        try:
            user = USER_MODEL.objects.get(phone=phone)
            if user.is_active:
                return user.password_reset_otp_generate(self.request)
            else:
                messages.warning(self, alert_messages.USER_NON_ACTIVE_MESSAGE)
        except USER_MODEL.DoesNotExist:
            messages.warning(self.request, alert_messages.PHONE_NOT_REGISTERED_MESSAGE)
            return redirect("accounts:password_reset")


class PasswordResetNewView(FormView):

    template_name = "accounts/password_reset_new.html"
    form_class = PasswordResetNewForm

    def form_valid(self, form):
        otp = form.cleaned_data.get('otp')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        user = USER_MODEL.objects.get(uuid=self.request.session["user_session_uuid"])

        otp_match = check_otp_2fa(otp=otp, otp_session_data=self.request.session['user_session_data'])
        if otp_match:
            user.set_password(password1)
            user.save()
            del self.request.session['user_session_uuid']
            del self.request.session['user_session_data']
            messages.success(self.request, "Password changed")
            login(self.request, user)
            return redirect("portal:home")
        else:
            messages.warning(self.request, "please enter correct OTP!")
            return redirect("accounts:password_reset_new")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    form_class = ProfileUpdateForm
    template_name = "accounts/profile_update.html"
    model = USER_MODEL
    success_url = reverse_lazy("accounts:profile_update")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, alert_messages.PROFILE_UPDATED_MESSAGE)
        return super().form_valid(form)

# class PasswordChange(LoginRequiredMixin, FormView):
#     form_class = PasswordChangeForm
#     template_name = "accounts/password_change.html"
#
#     def form_valid(self, form):
#         user = form.save()
#         update_session_auth_hash(self.request, user)  # Important!
#         messages.success(self.request, alert_messages.PASSWORD_CHANGED_SUCCESS_MESSAGE)
#         return redirect('portal:home')
