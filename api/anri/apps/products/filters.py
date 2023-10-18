import django_filters
from django_filters import rest_framework as filters

from anri.apps.products.models import Product


class ProductFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = Product
        fields = ["price", "tags", "group"]
