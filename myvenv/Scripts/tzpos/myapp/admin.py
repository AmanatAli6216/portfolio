from django.contrib import admin
from .models import *
# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['sup_name', 'phone', 'email', 'address']
    search_fields = ('sup_name', 'phone')
admin.site.register(Supplier, SupplierAdmin)