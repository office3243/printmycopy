from django.conf.urls import url
from . import views

app_name = 'payments'

urlpatterns = [
    url(r'^create_payment/$', views.create_payment, name='create_payment'),
    url(r'^success/$', views.payment_success, name='payment_success'),
    url(r'^failure/$', views.payment_failure, name='payment_failure')

]
