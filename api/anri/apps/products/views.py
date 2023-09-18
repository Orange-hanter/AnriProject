from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from anri.apps.products.models import Product
from anri.apps.products.serializer import ProductSerializer


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
