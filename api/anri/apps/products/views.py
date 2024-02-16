from django_filters.rest_framework import DjangoFilterBackend


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from anri.apps.products.models import Product, Tag
from anri.apps.common.pagination import CorePageNumberPagination
from anri.apps.products.serializers import ProductSerializer, TagSerializer, AdminActionProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = CorePageNumberPagination

    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ["name"]
    filterset_fields = ["tags", "group"]

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return Product.objects.order_by("created")

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response_data = {"result": serializer.data}
        return Response(response_data)

    def get_serializer_class(self):
        if self.action == "list":
            return ProductSerializer
        else:
            return AdminActionProductSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
