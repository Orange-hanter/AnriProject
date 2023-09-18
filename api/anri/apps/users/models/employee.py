from django.db import models

from anri.apps.common.models import CoreModel


class Employee(CoreModel):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    contragent = models.ForeignKey("Contragent", on_delete=models.CASCADE)
