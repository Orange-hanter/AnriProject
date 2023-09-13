from rest_framework import serializers

from anri.apps.products.models.product import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "name",
            "code",
            "group",
            "description",
            "quantity_in_stock",
            "price",
        )
