from django.conf.urls import url
from . import views

app_name = 'stations'


urlpatterns = [
    url(r'^list/$', views.StationListView.as_view(), name="list"),
]
