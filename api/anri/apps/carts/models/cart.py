from django.db import models

from anri.apps.common.models import CoreModel


class Cart(CoreModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
