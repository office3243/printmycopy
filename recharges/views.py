from recharges import alert_messages
from recharges.models import Recharge, OfferPack, CustomPack
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DetailView
from django.http import Http404
from payments.views import create_payment
import decimal
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def recharge_succeed(request, payment):
    messages.success(request, alert_messages.RECHARGE_SUCCEED_MESSAGE)
    return redirect("wallets:view")


@login_required
def recharge_failed(request, payment):
    messages.warning(request, alert_messages.RECHARGE_FAILED_MESSAGE)
    return redirect("wallets:view")


@login_required
def create_with_offer_pack(request, offer_pack_id):
    offer_pack = get_object_or_404(OfferPack, id=offer_pack_id, is_active=True)
    recharge = Recharge.objects.create(wallet=request.user.get_wallet, pack=offer_pack)
    return create_payment(request, recharge)


@login_required
def create_with_custom_pack(request):
    try:
        if request.method == "POST" :
            custom_price = decimal.Decimal(request.POST['custom_price'])
            if custom_price > 1.00:
                custom_pack = CustomPack.objects.create(price=custom_price, balance=decimal.Decimal(custom_price))
                recharge = Recharge.objects.create(wallet=request.user.get_wallet, pack=custom_pack)
                return create_payment(request, recharge)
        return redirect("wallets:view")
    except:
        return redirect("wallets:view")


class RechargeDetailView(LoginRequiredMixin, DetailView):

    template_name = 'recharges/detail.html'
    context_object_name = 'recharge'
    slug_url_kwarg = 'recharge_id'

    def get_object(self, queryset=None):
        return get_object_or_404(Recharge, pk=self.kwargs.get('recharge_id'), wallet__user=self.request.user)


class OfferPackDetailView(LoginRequiredMixin, DetailView):

    template_name = "recharges/offer_pack_detail.html"
    context_object_name = "offer_pack"
    slug_url_kwarg = "offer_pack_id"
    slug_field = "id"
    model = OfferPack

    def get_object(self, queryset=None):
        offer_pack = super().get_object()
        if offer_pack.is_active:
            return offer_pack
        else:
            raise Http404("Wrong Pack")
