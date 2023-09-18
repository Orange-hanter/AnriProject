from django.db import models

from anri.apps.common.models import CoreModel


class CartItem(CoreModel):
    cart_id = models.ForeignKey("Cart", on_delete=models.CASCADE)
    product_id = models.ForeignKey("Product")
    quantity = models.IntegerField()
