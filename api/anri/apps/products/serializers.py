from rest_framework import serializers

from anri.apps.products.models import Product, Tag


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("uuid", "name", "code", "group", "description", "quantity_in_stock", "price", "image", "tags")

    exclude = ("quantity_in_stock",)

    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        if "quantity_in_stock" in data:
            del data["quantity_in_stock"]
        return data


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)
