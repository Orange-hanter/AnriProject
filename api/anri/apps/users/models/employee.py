from django.db import models
from django.conf import settings

from anri.apps.common.models import CoreModel


class Employee(CoreModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contragent = models.ForeignKey("Contragent", on_delete=models.CASCADE)
