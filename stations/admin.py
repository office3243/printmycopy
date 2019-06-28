from django.contrib import admin
from .models import Station, StationClass
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Station, SimpleHistoryAdmin)
admin.site.register(StationClass)
# admin.site.register(SimpleHistoryAdmin)
