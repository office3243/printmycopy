from django.contrib import admin
from .models import Complaint, ComplaintCategory

admin.site.register(Complaint)
admin.site.register(ComplaintCategory)
