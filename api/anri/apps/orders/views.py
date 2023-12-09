from rest_framework import viewsets, mixins

from django.db.models import Q, F, Sum
from rest_framework.response import Response

from anri.apps.orders.choices import OrderStatus
from anri.apps.orders.models import OrderItem, Order
from anri.apps.orders.serializers import (
    OrderItemListSerializer,
    OrderItemCreateSerializer,
    OrderItemUpdateSerializer,
    OrderListSerializer,
    BaseOrderSerializer,
    OrderCreateSerializer,
)


class CartViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemListSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return OrderItemCreateSerializer
        if self.action == "update" or self.action == "partial_update":
            return OrderItemUpdateSerializer
        return OrderItemListSerializer

    def get_queryset(self):
        order, _ = Order.objects.filter(Q(user=self.request.user) & Q(status=OrderStatus.FORMATION)).get_or_create(
            user=self.request.user, amount=0
        )
        return OrderItem.objects.filter(order=order).annotate(products_price=F("quantity") * F("product__price"))

    def list(self, request, *args, **kwargs):
        """
        Returns all Products in the current User's shopping cart.
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            "result": serializer.data,
            "amount": queryset.aggregate(amount=Sum("products_price")).get("amount"),
        }
        return Response(response_data)


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return OrderCreateSerializer
        return OrderListSerializer

    def get_queryset(self):
        return Order.objects.filter(Q(user=self.request.user) & ~Q(status=OrderStatus.FORMATION))
