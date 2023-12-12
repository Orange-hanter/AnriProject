from django.db import models

from anri.apps.common.models import CoreModel


class DeliveryAddress(CoreModel):
    city = models.CharField(max_length=256)
    postcode = models.CharField(max_length=64)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.address
