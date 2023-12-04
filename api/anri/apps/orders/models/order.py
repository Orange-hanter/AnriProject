from django.db import models
from django.conf import settings


from anri.apps.common.models import CoreModel
from anri.apps.orders.choices import OrderStatus, PaymentMethod


class Order(CoreModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    address = models.CharField(max_length=256)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=64, choices=OrderStatus.choices, default=OrderStatus.FORMATION)
    payment_method = models.CharField(max_length=64, choices=PaymentMethod.choices, default=PaymentMethod.ONLINE)
