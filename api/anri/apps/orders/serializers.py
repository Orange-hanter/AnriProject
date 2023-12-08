from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from anri.apps.orders.choices import OrderStatus
from anri.apps.orders.models import OrderItem, Order
from anri.apps.products.serializers import ProductSerializer


class BaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("uuid", "product", "quantity")

    def save(self, **kwargs):
        if self.validated_data["quantity"] > self.validated_data["product"].quantity_in_stock:
            raise ValidationError(
                {
                    "quantity": "Quantity must be less than quantity_in_stock.",
                    "quantity_in_stock": f"{self.validated_data['product'].quantity_in_stock}",
                }
            )
        return super().save(**kwargs)


class OrderItemCreateSerializer(BaseOrderItemSerializer):
    uuid = serializers.ReadOnlyField()

    def create(self, validated_data):
        order = Order.objects.filter(Q(user=self.context["request"].user) & Q(status=OrderStatus.FORMATION)).get()
        validated_data["order"] = order
        return super().create(validated_data)


class OrderItemUpdateSerializer(BaseOrderItemSerializer):
    uuid = serializers.ReadOnlyField()

    class Meta(BaseOrderItemSerializer.Meta):
        fields = ("uuid", "quantity")


class OrderItemListSerializer(BaseOrderItemSerializer):
    product = ProductSerializer()
    products_price = serializers.SerializerMethodField()

    class Meta(BaseOrderItemSerializer.Meta):
        fields = BaseOrderItemSerializer.Meta.fields + ("products_price",)

    def get_products_price(self, obj):
        return obj.products_price


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("amount", "address", "paid", "status", "payment_method")
