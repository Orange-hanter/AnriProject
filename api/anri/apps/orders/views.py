from datetime import timedelta

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from anri.apps.orders.models import Order, OrderItem
from anri.apps.carts.models import CartItem
from anri.apps.orders.serializers import OrderItemSerializer, OrderSerializer
from .choices import OrderStatus
from .tasks import delete_order


class OrderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        cart_items = CartItem.objects.filter(user=request.user).select_related("product")
        total_amount = sum([cart_item.product.price * cart_item.quantity for cart_item in cart_items])
        order = Order.objects.create(user=request.user, total_amount=total_amount, status=OrderStatus.PAYMENT_WAITING)
        order_items = [
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price,
                subtotal=cart_item.product.price * cart_item.quantity,
            )
            for cart_item in cart_items
        ]
        delete_order.apply_async(args=[order.uuid], countdown=timedelta(minutes=15).seconds)
        return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
