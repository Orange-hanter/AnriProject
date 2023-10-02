from rest_framework import serializers

from anri.apps.carts.models import CartItem
from anri.apps.products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            "uuid",
            "product",
            "quantity",
        )

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class CartSerializer(serializers.ModelSerializer):
    products_cost = serializers.SerializerMethodField()
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = (
            "uuid",
            "user",
            "product",
            "quantity",
            "products_cost",
        )

    def get_products_cost(self, obj):
        return obj.products_cost
