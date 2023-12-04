from django.contrib import admin

from anri.apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "address", "paid", "status", "payment_method")
