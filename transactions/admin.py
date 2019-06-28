from django.contrib import admin
from .models import Transaction, File


class FileAdmin(admin.ModelAdmin):
    list_display = ("__str__", "input_file", "converted_file")


admin.site.register(Transaction)
admin.site.register(File, FileAdmin)

