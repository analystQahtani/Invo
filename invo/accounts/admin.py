from django.contrib import admin

from accounts.models import Client, Domain
from django_tenants.admin import TenantAdminMixin

# Register your models here.
class DomainInline(admin.TabularInline):
    model = Domain
    max_num = 1

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = (
        "name",
        "created_on",
        "user"
        
        )
        inlines = [DomainInline]
        
