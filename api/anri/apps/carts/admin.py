from django.contrib import admin
from anri.apps.carts.models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity")
    list_filter = ("user",)
