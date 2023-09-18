from django.db import models

from anri.apps.common.models import CoreModel


class Order(CoreModel):
    user = models.OneToOneField("User")
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField()
    status = models.CharField(max_length=127)
