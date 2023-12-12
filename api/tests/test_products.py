import os
import json
import pytest

from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from anri.settings.django import MEDIA_ROOT
from anri.apps.products.models import Product, Tag


# Возвращает изображение, готовое для использования в продукте
@pytest.fixture
def get_test_image():
    small_gif = (
        b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04"
        b"\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02"
        b"\x02\x4c\x01\x00\x3b"
    )

    uploaded = SimpleUploadedFile("small.jpg", small_gif, content_type="image")

    return uploaded


# Возвращает тестового пользователя, который верифицирован(через почту)
@pytest.fixture
def get_verified_user():
    return User.objects.create_user(
        username="test_user", email="user@test.com", password="test_password", is_active=True
    )


# Возвращает тестового пользователя, который не верифицирован
@pytest.fixture
def get_unverified_user():
    return User.objects.create_user(
        username="test_user_not_verified", email="user@test.com", password="test_password_not_verified", is_active=False
    )


# Возвращает тестового админ-пользователя со всеми правами
@pytest.fixture
def get_super_user():
    return User.objects.create_superuser(
        username="test_super_user", email="super_user@test.com", password="superuser", is_active=True
    )


# Возвращает тестовый тег для продукта
@pytest.fixture
def product_tag():
    return Tag.objects.create(name="product_tag")


# Возвращает тестовый продукт
@pytest.fixture
def first_product(product_tag):
    return Product.objects.create(name="first_product", quantity_in_stock=10, price=250)


# Возвращает тестовый продукт
@pytest.fixture
def second_product(product_tag):
    return Product.objects.create(name="second_product", quantity_in_stock=10, price=250)


# Возвращает тестовый продукт который имеет теги
@pytest.fixture
def test_group_tag_product(product_tag):
    obj = Product.objects.create(name="test_product", group="test", quantity_in_stock=10, price=250)
    obj.tags.set([product_tag.uuid])
    return obj


# Возвращает пару параметров, где 1 параметр - то, что ищем, второй - ожидаемый результат(кол-во найденных продуктов)
@pytest.fixture(
    params=[
        ("test_nothing", 0),
        ("test_product", 1),
    ]
)
def test_ready_search(request):
    return request.param


# Возвращает пару параметров, где 1 параметр - то, что мы ищем фильтруя по группам, второй - ожидаемый результат(кол-во найденных продуктов)
@pytest.fixture(
    params=[
        ("test_nothing", 0),
        ("test", 1),
    ]
)
def test_group_filter(request):
    return request.param


# Вовращает кортеж параметров, где 1 параметр - то, что мы ищем фильтруя по тегам, второй - ожидаемый результат(кол-во найденных продуктов),
#  третий - код возврата(в реализации так, что в случае отсутствия код возврата - 400)
@pytest.fixture(
    params=[
        ("test", False, 400),
        ("", 1, 200),
    ]
)
def test_tag_filter(request):
    return request.param


# Тестовый сценарий, который проверяет get-запрос по продуктам(т.е вернуть просто список продуктов)
# Идет проверка по 3 видам пользователей, код возврата обязан быть одинаковым(логика такова, что все должны иметь возможность просмотреть продукты)
@pytest.mark.django_db
@pytest.mark.parametrize(
    "user, status_code", [("get_verified_user", 200), ("get_unverified_user", 200), ("get_super_user", 200)]
)
def test_product_list(request, client, user, status_code, first_product):
    current_user = request.getfixturevalue(user)
    client.force_login(current_user)
    expected_data = {
        "result": [
            {
                "uuid": f"{first_product.uuid}",
                "name": first_product.name,
                "code": "",
                "group": "",
                "description": "",
                "price": "{:.2f}".format(first_product.price),
                "image": None,
                "tags": [],
            },
        ]
    }
    url = reverse("api-v1-products:product-list")
    response = client.get(url)
    response_data = json.loads(json.dumps(response.data))

    assert response_data == expected_data
    assert response.status_code == status_code


# Тестовый сценарий, который проверяет post-запрос по продуктам(т.е возможность создать продукт)
# Создать может только администратор(201 код возврата), остальные должны быть либо 403 - запрещен доступ, или 401 - не верифицирован
@pytest.mark.django_db
@pytest.mark.parametrize(
    "user, status_code", [("get_verified_user", 403), ("get_unverified_user", 401), ("get_super_user", 201)]
)
def test_create_product(request, client, user, status_code, product_tag, get_test_image):
    client.force_login(request.getfixturevalue(user))

    data = {
        "name": "Test product item",
        "code": "401212",
        "group": "Any",
        "description": "Test item",
        "quantity_in_stock": 10,
        "price": 100.00,
        "image": get_test_image,
        "tags": [product_tag.uuid],
    }

    url = reverse("api-v1-products:product-list")
    response = client.post(url, data=data)

    assert response.status_code == status_code
    if status_code == 201:
        assert response.data["code"] == "401212"
        os.remove(f"{MEDIA_ROOT}/img/{get_test_image.name}")


# Тестовый сценарий, в котором проверяется возможность поиска по продуктам(выполнять такой запрос могут все)
# Однако, результат будет отличаться в зависимости от того, существует ли данный продукт, т.е код возврата всегда 200
# Здесь 6 тест-кейсов, 3 пользователя и 2 случая, позитивный и негативный(существует продукт или нет)
@pytest.mark.django_db
@pytest.mark.parametrize("user", ["get_verified_user", "get_unverified_user", "get_super_user"])
def test_search_item(request, client, user, test_ready_search, test_group_tag_product):
    (search, result) = test_ready_search
    client.force_login(request.getfixturevalue(user))
    url = reverse("api-v1-products:product-list")
    response = client.get(url, {"search": search})
    if result:
        assert response.data["result"][0]["group"] == test_group_tag_product.group
    else:
        assert len(response.data["result"]) == result

    assert response.status_code == 200


# Тестовый сценарий, в котором проверяется возможность фильтрации по группам(выполнять такой запрос могут все)
# Однако, результат будет отличаться в зависимости от того, существует ли данный продукт, т.е код возврата всегда 200
# Здесь 6 тест-кейсов, 3 пользователя и 2 случая, позитивный и негативный(существует продукт или нет)
@pytest.mark.django_db
@pytest.mark.parametrize("user", ["get_verified_user", "get_unverified_user", "get_super_user"])
def test_filter_by_group(request, client, user, test_group_filter, test_group_tag_product):
    (group, result) = test_group_filter
    client.force_login(request.getfixturevalue(user))

    url = reverse("api-v1-products:product-list")
    response = client.get(url, {"group": group})

    if result:
        assert response.data["result"][0]["name"] == test_group_tag_product.name
    else:
        assert len(response.data["result"]) == result

    assert response.status_code == 200


# Тестовый сценарий в котором проверяется возможность фильтрации по тегам(выполнять такой запрос могут все)
# Однако, результат будет отличаться в зависимости от того, существует ли данный продукт, при этом код возврата отличается
# Здесь 6 тест-кейсов, 3 пользователя и 2 случая, позитивный и негативный(существует продукт или нет)
@pytest.mark.django_db
@pytest.mark.parametrize("user", ["get_verified_user", "get_unverified_user", "get_super_user"])
def test_filter_by_tag(request, client, user, test_tag_filter, test_group_tag_product, product_tag):
    (addition_to_tag, result, status_code) = test_tag_filter
    client.force_login(request.getfixturevalue(user))

    url = reverse("api-v1-products:product-list")
    response = client.get(url, {"tags": f"{product_tag.uuid}{addition_to_tag}"})

    if result:
        assert response.data["result"][0]["name"] == test_group_tag_product.name
    else:
        assert response.data["tags"] == [f"“{product_tag.uuid}{addition_to_tag}” is not a valid UUID."]

    assert response.status_code == status_code


# Тестовый сценарий в котором проверяется возможность выполнять patch-запрос, то есть изменять какое-либо значение в уже существующем продукте
# Выполнять данный запрос может только администратор(код возврата 200), остальные же либо 403 - запрещен доступ для верифицированного пользователя, либо 401(non authenticated) не верифицирован
@pytest.mark.django_db
@pytest.mark.parametrize(
    "user, status_code", [("get_verified_user", 403), ("get_unverified_user", 401), ("get_super_user", 200)]
)
def test_patch_product(request, client, user, status_code, first_product, name="test_change_product"):
    client.force_login(request.getfixturevalue(user))
    data = {"name": name}
    url = f"{reverse('api-v1-products:product-detail', args=[first_product.uuid])}"
    response = client.patch(url, data=data, content_type="application/json")

    assert response.status_code == status_code
    if response.status_code == 200:
        assert response.data["name"] == data["name"]


# Тестовый сценарий в котором проверяется возможность выполнять put-запрос, то есть изменить продукт полностью
# Выполнять данный запрос может только администратор(код возврата 200), остальные же либо 403 - запрещен доступ для верифицированного пользователя, либо 401(non authenticated) не верифицирован
@pytest.mark.django_db
@pytest.mark.parametrize(
    "user, status_code", [("get_verified_user", 403), ("get_unverified_user", 401), ("get_super_user", 200)]
)
def test_put_product(request, user, status_code, first_product, get_test_image, product_tag, client=APIClient()):
    client.force_login(request.getfixturevalue(user))

    data = {
        "name": "test_".join(first_product.name),
        "group": "test_group",
        "price": 100.00,
        "code": "test_qwerty",
        "image": get_test_image,
        "description": "test product",
        "quantity_in_stock": 10,
        "tags": [product_tag.uuid],
    }

    url = reverse("api-v1-products:product-detail", args=[first_product.uuid])

    response = client.put(url, data=data)
    print(response)
    assert response.status_code == status_code


# Тестовый сценарий в котором проверяется возможность выполнять delete-запрос, то есть удалить продукт
# Выполнять данный запрос может только администратор(код возврата 200), остальные же либо 403 - запрещен доступ для верифицированного пользователя, либо 401(non authenticated) не верифицирован
@pytest.mark.django_db
@pytest.mark.parametrize(
    "user, status_code", [("get_verified_user", 403), ("get_unverified_user", 401), ("get_super_user", 204)]
)
def test_delete_product(request, client, user, status_code, first_product):
    client.force_login(request.getfixturevalue(user))
    url = f"{reverse('api-v1-products:product-detail', args=[first_product.uuid])}"
    response = client.delete(url)
    assert response.status_code == status_code
