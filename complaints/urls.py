from django.conf.urls import url
from . import views
from .forms import ComplaintAddForm


app_name = "complaints"

urlpatterns = [

    url(r'^list/$', views.ComplaintListView.as_view(), name="list"),
    url(r'^add/$', views.ComplaintAddView.as_view(), name='add'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.ComplaintUpdateView.as_view(), name="update"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.ComplaintDeleteView.as_view(), name="delete"),

]
