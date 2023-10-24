from django.db import models
from django.conf import settings


from anri.apps.common.models import CoreModel
from ..choices import OrderStatus


class Order(CoreModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=100, decimal_places=2)
    status = models.CharField(max_length=64, choices=OrderStatus.choices, default=OrderStatus.FORMATION)
