from django.contrib import admin
from anri.apps.orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "total_amount", "status")
    list_filter = ("user",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "price", "subtotal")
    list_filter = (
        "order",
        "product",
    )
