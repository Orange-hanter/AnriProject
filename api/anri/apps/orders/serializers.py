from rest_framework import serializers

from anri.apps.orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("order", "product", "quantity", "subtotal")


class OrderSerializer(serializers.ModelSerializer):
    total_amount = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ("total_amount", "status")
