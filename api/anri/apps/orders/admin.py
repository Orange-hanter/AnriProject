from django.contrib import admin
from anri.apps.orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "order_date", "total_amount", "status")
    list_filter = (
        "order_date",
        "user",
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "price_at_order_time", "subtotal")
    list_filter = (
        "order",
        "product",
    )
