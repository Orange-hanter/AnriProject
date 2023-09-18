from django.db import models

from anri.apps.common.models import CoreModel
from anri.apps.products.models.orders import Order
from anri.apps.products.models.products import Product


class OrderItem(CoreModel):
    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_order_time = models.DecimalField()
    subtotal = models.DecimalField()
