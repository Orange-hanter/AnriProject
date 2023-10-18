import pytest

from anri.apps.products.models import Product, Tag


@pytest.fixture
def product_tag():
    return Tag.objects.create(name="product_tag")


@pytest.fixture
def first_product(product_tag):
    return Product.objects.create(name="first_product", quantity_in_stock=10, price=250)


@pytest.fixture
def second_product(product_tag):
    return Product.objects.create(name="second_product", quantity_in_stock=10, price=250)
