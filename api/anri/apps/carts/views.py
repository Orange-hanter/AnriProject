from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import F, Sum

from anri.apps.carts.models import CartItem
from anri.apps.carts.serializers import CartItemSerializer, CartSerializer, CartItemUpdateSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        queryset = CartItem.objects.filter(user=self.request.user).annotate(
            products_cost=F("product__price") * F("quantity")
        )
        return queryset

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return CartSerializer
        elif self.action == "update" or self.action == "partial_update":
            return CartItemUpdateSerializer
        return CartItemSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response_data = {"result": serializer.data}
        response_data["total_cost"] = queryset.aggregate(total_cost=Sum("products_cost")).get("total_cost")
        return Response(response_data)
