from django.contrib import admin
from .models import Item, Expense
from accounts.models import Client, Domain
from django_tenants.admin import TenantAdminMixin

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
        list_display = (
        "name",
        "date",
        "amount",
        "description"
        
        )
       

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
        list_display = (
        "name",
        "price",
        
        )
  