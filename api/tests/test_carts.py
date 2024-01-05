from decimal import Decimal
import pytest

from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

from anri.apps.orders.models import OrderItem, Order
from anri.apps.orders.serializers import OrderItemUpdateSerializer
from tests.test_products import first_product, second_product, product_tag


@pytest.fixture
def user():
    return User.objects.create_user(username="user", password="test_pass")


@pytest.fixture()
def order(user):
    return Order.objects.create(user=user, amount=0)


@pytest.fixture
def first_cart_item(first_product, order):
    return OrderItem.objects.create(order=order, product=first_product, quantity=10)


@pytest.fixture
def second_cart_item(second_product, order):
    return OrderItem.objects.create(order=order, product=second_product, quantity=10)


@pytest.mark.django_db
def test_add_item_to_cart(client, user, first_product):
    client.force_login(user)
    data = {"product": f"{first_product.uuid}", "quantity": 10}
    url = reverse("api-v1-carts:cart-list")
    response = client.post(url, data=data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_add_item_to_cart_quantity_qt_in_stock(client, user, first_product):
    client.force_login(user)
    data = {"product": f"{first_product.uuid}", "quantity": 20}
    url = reverse("api-v1-carts:cart-list")
    response = client.post(url, data=data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_cart_list(client, user, first_product, first_cart_item, second_product, second_cart_item):
    client.force_login(user)
    expected_data = {
        "result": [
            {
                "uuid": f"{first_cart_item.uuid}",
                "product": {
                    "uuid": f"{first_product.uuid}",
                    "name": first_product.name,
                    "code": "",
                    "group": "",
                    "description": "",
                    "price": "250.00",
                    "image": None,
                    "tags": [],
                },
                "quantity": 10,
                "products_price": Decimal("2500.00"),
            },
            {
                "uuid": f"{second_cart_item.uuid}",
                "product": {
                    "uuid": f"{second_product.uuid}",
                    "name": second_product.name,
                    "code": "",
                    "group": "",
                    "description": "",
                    "price": "250.00",
                    "image": None,
                    "tags": [],
                },
                "quantity": 10,
                "products_price": Decimal("2500.00"),
            },
        ],
        "amount": Decimal("5000.00"),
    }

    url = reverse("api-v1-carts:cart-list")
    response = client.get(url)
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_put_cart_item(client, user, first_cart_item, first_product):
    client.force_login(user)
    data = {"product": f"{first_product.uuid}", "quantity": 10}
    expected_data = OrderItemUpdateSerializer(first_cart_item).data
    url = f"{reverse('api-v1-carts:cart-detail', args=[first_cart_item.uuid])}"
    response = client.put(url, data=data, content_type="application/json")
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_patch_cart_item(client, user, first_cart_item, first_product):
    client.force_login(user)
    data = {"product": f"{first_product.uuid}", "quantity": 10}
    expected_data = OrderItemUpdateSerializer(first_cart_item).data
    url = f"{reverse('api-v1-carts:cart-detail', args=[first_cart_item.uuid])}"
    response = client.patch(url, data=data, content_type="application/json")
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_delete_cart_item(client, user, first_cart_item):
    client.force_login(user)
    url = f"{reverse('api-v1-carts:cart-detail', args=[first_cart_item.uuid])}"
    response = client.delete(url)
    assert response.status_code == 204
