from django.db.models import Q, F, Sum
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from anri.apps.orders.choices import OrderStatus, PaymentMethod
from anri.apps.orders.models import OrderItem, Order, DeliveryAddress
from anri.apps.products.serializers import ProductSerializer
from anri.apps.users.models import UserInfo
from anri.apps.users.serializers import UserInfoSerializer


class BaseOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("uuid", "product", "quantity")

    def save(self, **kwargs):
        if self.validated_data["quantity"] > self.validated_data["product"].quantity_in_stock:
            raise ValidationError(
                {
                    "quantity": "Quantity must be less than quantity_in_stock.",
                    "quantity_in_stock": f"{self.validated_data['product'].quantity_in_stock}",
                }
            )
        return super().save(**kwargs)


class OrderItemCreateSerializer(BaseOrderItemSerializer):
    uuid = serializers.ReadOnlyField()

    def create(self, validated_data):
        order = Order.objects.filter(Q(user=self.context["request"].user) & Q(status=OrderStatus.FORMATION)).get()
        validated_data["order"] = order
        return super().create(validated_data)


class OrderItemUpdateSerializer(BaseOrderItemSerializer):
    uuid = serializers.ReadOnlyField()

    class Meta(BaseOrderItemSerializer.Meta):
        fields = ("uuid", "quantity")


class OrderItemListSerializer(BaseOrderItemSerializer):
    product = ProductSerializer()
    products_price = serializers.SerializerMethodField()

    class Meta(BaseOrderItemSerializer.Meta):
        fields = BaseOrderItemSerializer.Meta.fields + ("products_price",)

    def get_products_price(self, obj):
        return obj.products_price


class NestedOrderItemSerializer(BaseOrderItemSerializer):
    class Meta(BaseOrderItemSerializer.Meta):
        fields = BaseOrderItemSerializer.Meta.fields + ("price",)


class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = ("city", "postcode", "address")


class BaseOrderSerializer(serializers.ModelSerializer):
    contacts = UserInfoSerializer()

    class Meta:
        model = Order
        fields = ("uuid", "amount", "address", "paid", "status", "payment_method", "contacts")


class OrderListSerializer(BaseOrderSerializer):
    contacts = UserInfoSerializer(read_only=True)
    order_items = NestedOrderItemSerializer(many=True)

    class Meta(BaseOrderSerializer.Meta):
        fields = BaseOrderSerializer.Meta.fields + ("order_items",)


class OrderCreateSerializer(BaseOrderSerializer):
    amount = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()
    paid = serializers.ReadOnlyField()
    address = DeliveryAddressSerializer()

    def save(self, **kwargs):
        contacts = self.validated_data.get("contacts")
        contacts["user"] = self.context["request"].user
        contacts, _ = UserInfo.objects.get_or_create(**contacts)
        address = self.validated_data.get("address")
        address = DeliveryAddress.objects.create(**address)

        ModelClass = self.Meta.model
        instance = ModelClass.objects.get(user=self.context["request"].user, status=OrderStatus.FORMATION)

        items = instance.order_items.annotate(new_price=F("product__price") * F("quantity"))
        for item in items:
            item.price = item.new_price
        OrderItem.objects.bulk_update(items, ["price"])

        amount = ModelClass.objects.aggregate(sum=Sum("order_items__price")).get("sum")
        instance.amount = amount
        instance.address = address
        instance.payment_method = self.validated_data["payment_method"]
        if self.validated_data["payment_method"] == PaymentMethod.ONLINE:
            instance.status = OrderStatus.PAYMENT_WAITING
        else:
            instance.status = OrderStatus.DISPATCH_WAITING
        instance.save()
        return instance
