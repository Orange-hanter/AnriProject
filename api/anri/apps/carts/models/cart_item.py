from django.db import models
from django.conf import settings

from anri.apps.common.models import CoreModel


class CartItem(CoreModel):
    cart = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
