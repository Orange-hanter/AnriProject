from rest_framework import serializers

from anri.apps.orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("order", "product", "quantity", "subtotal")
