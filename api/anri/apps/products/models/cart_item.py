from django.db import models

from anri.apps.common.models import CoreModel


class CartItem(CoreModel):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("Product")
    quantity = models.IntegerField()
