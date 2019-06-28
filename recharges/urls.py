from django.conf.urls import url
from . import views

app_name = 'recharges'


urlpatterns = [
    url(r'^details/(?P<recharge_id>[0-9]+)/$', views.RechargeDetailView.as_view(), name='detail'),

    url(r"^offer_pack/detail/(?P<offer_pack_id>[0-9]+)/$", views.OfferPackDetailView.as_view(), name="offer_pack_detail"),

    url(r'^create/offer_pack/(?P<offer_pack_id>[0-9]+)/$', views.create_with_offer_pack, name='create_with_offer_pack'),
    url(r'^create/custom_pack/$', views.create_with_custom_pack, name='create_with_custom_pack'),
    ]
