from django.db import models

from anri.apps.common.models import CoreModel


class Product(CoreModel):
    name = models.CharField(max_length=127)
    code = models.CharField(max_length=127)
    group = models.CharField(max_length=127)
    description = models.CharField(max_length=127)
    quantity_in_stock = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
