from django.db import models

from anri.apps.common.models import CoreModel


class Product(CoreModel):
    name = models.CharField(max_length=127)
    code = models.CharField(max_length=127)
    group = models.CharField(max_length=127)
    description = models.CharField(max_length=512)
    tags = models.ManyToManyField("products.Tag")
    image = models.ImageField("Image", upload_to="img")
    quantity_in_stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
