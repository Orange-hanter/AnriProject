from django.db import models

from anri.apps.common.models import CoreModel


class Employee(CoreModel):
    user_id = models.ForeignKey("User")
    contragent_id = models.ForeignKey("Contragent")
