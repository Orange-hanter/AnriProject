from rest_framework import serializers

from anri.apps.products.models import Product, Tag


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("uuid", "name", "code", "group", "description", "quantity_in_stock", "price", "image", "tags")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)
