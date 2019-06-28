"""ewayprint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('accounts.urls', namespace='accounts')),
    url(r'', include('portal.urls', namespace='portal')),
    url(r'^transactions/', include('transactions.urls', namespace='transactions')),
    url(r'^wallets/', include('wallets.urls', namespace='wallets')),
    url(r'^payments/', include('payments.urls', namespace='payments')),
    url(r'^recharges/', include('recharges.urls', namespace='recharges')),
    url(r'^complaints/', include('complaints.urls', namespace='complaints')),
    url(r'^stations/', include('stations.urls', namespace='stations')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
