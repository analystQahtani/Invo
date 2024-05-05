from django.contrib import admin

from accounts.models import Client, Domain
from django_tenants.admin import TenantAdminMixin

class ControlAdmin(admin.ModelAdmin):
        list_display = (
        "name",
        "price",
        "client"
        
        )
       
        