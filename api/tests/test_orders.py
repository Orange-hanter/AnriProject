import pytest

from django.test import Client
from django.urls import reverse

from anri.apps.orders.models import Order
from anri.apps.orders.choices import OrderStatus

from tests.test_products import get_super_user, get_verified_user, first_product, second_product, product_tag
from tests.test_carts import first_cart_item, second_cart_item, order, user


@pytest.mark.django_db
def test_post_order(client, first_cart_item, second_cart_item, user):
    client.force_login(user)

    # url_check = reverse("api-v1-carts:cart-list")
    # response_check = client.get(url_check)
    # print(response_check.data)

    url = reverse("api-v1-carts:order-list")

    data = {
        "address": {"city": "aa", "postcode": "123456", "address": "asd"},
        "payment_method": "ONLINE",
        "contacts": {"company": "aa", "name": "aa", "phone": "+375331235678"},
    }

    response = client.post(url, data=data)

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_order(client, user, first_cart_item, order):
    client.force_login(user)

    order.status = OrderStatus.PAYMENT_WAITING
    url = f"{reverse('api-v1-carts:order-detail', args=[order.uuid])}"
    print(order.status)
    print(order.uuid)
    response = client.delete(url)
    print(response.data)
    assert response.status_code == 204


@pytest.mark.django_db
def test_get_all_orders(client, user, first_cart_item, order):
    client.force_login(user)
    url = reverse("api-v1-carts:order-list")

    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_order_by_id(client, user, first_cart_item, order):
    client.force_login(user)
    url = reverse("api-v1-carts:order-list")

    response = client.get(url, args=[order.uuid])

    assert response.status_code == 200
