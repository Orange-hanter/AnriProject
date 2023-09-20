from django.db import models

from anri.apps.common.models import CoreModel


class OrderItem(CoreModel):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    # product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_at_order_time = models.DecimalField(max_digits=5, decimal_places=2)
    subtotal = models.DecimalField(max_digits=5, decimal_places=2)
