from django.contrib import admin

from anri.apps.products.models import Product, Tag


class TagInline(admin.TabularInline):
    model = Product.tags.through


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "group",
        "description",
        "quantity_in_stock",
        "price",
    )
    list_filter = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    inlines = (TagInline,)
