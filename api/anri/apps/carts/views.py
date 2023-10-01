from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import F, Sum

from anri.apps.carts.models import CartItem
from anri.apps.carts.serializers import CartItemSerializer, CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def list(self, request, *args, **kwargs):
        queryset = CartItem.objects.filter(user=request.user).annotate(
            products_cost=F("product__price") * F("quantity")
        )
        serializer = CartSerializer(queryset, many=True)
        response_data = {"result": serializer.data}
        response_data["total_cost"] = queryset.aggregate(total_cost=Sum("products_cost")).get("total_cost")
        return Response(response_data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

    def retrieve(self, request, *args, **kwargs):
        queryset = CartItem.objects.filter(user=request.user).annotate(
            products_cost=F("product__price") * F("quantity")
        )
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)
