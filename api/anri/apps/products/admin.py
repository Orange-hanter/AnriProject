from django.contrib import admin

from anri.apps.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "group", "description", "quantity_in_stock", "price")
    list_filter = ("name",)
