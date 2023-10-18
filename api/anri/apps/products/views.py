from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from anri.apps.products.models import Product
from anri.apps.products.serializer import ProductSerializer
from anri.apps.products.filters import ProductFilter


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.order_by("created")
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    search_fields = ["name"]
    filter_backends = (filters.SearchFilter,)
    filterset_class = ProductFilter

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
