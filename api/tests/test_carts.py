from decimal import Decimal
import pytest

from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

from anri.apps.carts.models import CartItem
from anri.apps.carts.serializers import CartItemUpdateSerializer

from tests.test_products import first_product, second_product, product_tag


@pytest.fixture
def user():
    return User.objects.create_user(username="user", password="test_pass")


@pytest.fixture
def first_cart_item(first_product, user):
    return CartItem.objects.create(user=user, product=first_product, quantity=10)


@pytest.fixture
def first_cart_item_guantity_qt_in_stock(first_product, user):
    return CartItem.objects.create(user=user, product=first_product, quantity=first_product.quantity_in_stock + 10)


@pytest.fixture
def second_cart_item(second_product, user):
    return CartItem.objects.create(user=user, product=second_product, quantity=10)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "quantity",
    [
        10,
        20,
    ],
)
def test_add_item_to_cart(client, user, first_product, quantity):
    client.force_login(user)
    data = {"product": f"{first_product.uuid}", "quantity": f"{quantity}"}
    url = reverse("api-v1-carts:cart-list")
    response = client.post(url, data=data)
    assert response.status_code == 201
    assert response.data["quantity"] == 10


@pytest.mark.django_db
def test_cart_list(client, user, first_product, first_cart_item, second_product, second_cart_item):
    client.force_login(user)
    expected_data = {
        "result": [
            {
                "uuid": f"{first_cart_item.uuid}",
                "user": first_cart_item.user.id,
                "product": {
                    "uuid": f"{first_product.uuid}",
                    "name": first_product.name,
                    "code": "",
                    "group": "",
                    "description": "",
                    "quantity_in_stock": 10,
                    "price": "250.00",
                    "image": None,
                    "tags": [],
                },
                "quantity": 10,
                "products_cost": Decimal("2500.00"),
            },
            {
                "uuid": f"{second_cart_item.uuid}",
                "user": second_cart_item.user.id,
                "product": {
                    "uuid": f"{second_product.uuid}",
                    "name": second_product.name,
                    "code": "",
                    "group": "",
                    "description": "",
                    "quantity_in_stock": 10,
                    "price": "250.00",
                    "image": None,
                    "tags": [],
                },
                "quantity": 10,
                "products_cost": Decimal("2500.00"),
            },
        ],
        "total_cost": Decimal("5000.00"),
    }

    url = reverse("api-v1-carts:cart-list")
    response = client.get(url)
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
@pytest.mark.parametrize(
    "quantity",
    [
        10,
        20,
    ],
)
def test_put_cart_item(client, user, first_cart_item, first_product, quantity):
    client.force_login(user)
    data = {"product": f"{first_product.uuid}", "quantity": quantity}
    expected_data = CartItemUpdateSerializer(first_cart_item).data
    url = f"{reverse('api-v1-carts:cart-detail', args=[first_cart_item.uuid])}"
    response = client.put(url, data=data, content_type="application/json")
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
@pytest.mark.parametrize(
    "quantity",
    [
        10,
        20,
    ],
)
def test_patch_cart_item(client, user, first_cart_item, first_product, quantity):
    client.force_login(user)
    data = {"product": f"{first_product.uuid}", "quantity": quantity}
    expected_data = CartItemUpdateSerializer(first_cart_item).data
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
