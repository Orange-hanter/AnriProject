from rest_framework import serializers

from anri.apps.products.models import Product, Tag


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("uuid", "name", "code", "group", "description", "price", "image", "tags")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)
