from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from anri.apps.products.models import Product, Tag
from anri.apps.common.pagination import CorePageNumberPagination
from anri.apps.products.serializers import ProductSerializer, TagSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.order_by("created")
    serializer_class = ProductSerializer
    pagination_class = CorePageNumberPagination

    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ["name"]
    filterset_fields = ["tags", "group"]

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
