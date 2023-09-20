from django.db import models
from django.conf import settings


from anri.apps.common.models import CoreModel


class Order(CoreModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=127)
