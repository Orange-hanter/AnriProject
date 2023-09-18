from django.db import models

from anri.apps.common.models import CoreModel
from anri.apps.products.models.user import User


class Cart(CoreModel):
    user_id = models.OneToOneField(User.uuid, on_delete=models.CASCADE)
