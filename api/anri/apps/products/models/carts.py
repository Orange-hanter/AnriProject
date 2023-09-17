from django.db import models

from anri.apps.common.models import CoreModel
from anri.apps.products.models.users import User


class Cart(CoreModel):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
