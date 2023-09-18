from django.db import models

from anri.apps.common.models import CoreModel


class Employee(CoreModel):
    user = models.ForeignKey("User")
    contragent = models.ForeignKey("Contragent")
