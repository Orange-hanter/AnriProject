from rest_framework import serializers

from anri.apps.products.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "code", "group", "description", "quantity_in_stock", "price", "image", "tags")
