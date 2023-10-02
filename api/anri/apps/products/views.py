from rest_framework import viewsets

from anri.apps.products.models import Product, Tag
from anri.apps.common.pagination import CorePageNumberPagination
from anri.apps.products.serializers import ProductSerializer, TagSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CorePageNumberPagination


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
