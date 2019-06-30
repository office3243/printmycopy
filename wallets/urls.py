from django.conf.urls import url
from . import views

app_name = 'wallets'


urlpatterns = [
    url(r'^$', views.WalletView.as_view(), name='view'),
]
