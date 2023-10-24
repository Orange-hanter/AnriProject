from django.db import models

from anri.apps.common.models import CoreModel


class OrderItem(CoreModel):
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    subtotal = models.DecimalField(max_digits=100, decimal_places=2)
