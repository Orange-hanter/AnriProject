from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

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
    search_fields = [
        "name",
        "group",
        "tag",
    ]
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        queryset = Product.objects.filter().order_by("price")
        return queryset

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response_data = {"result": serializer.data}
        return Response(response_data)
