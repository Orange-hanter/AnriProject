from django.db import models

from anri.apps.common.models import CoreModel
from anri.apps.products.models.users import User


class Order(CoreModel):
    user_id = models.OneToOneField(User)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField()
    status = models.CharField(max_length=127)
