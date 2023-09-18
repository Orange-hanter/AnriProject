from django.db import models

from anri.apps.products.models.user import User
from anri.apps.products.models.contragents import Contragent
from anri.apps.common.models import CoreModel


class Employee(CoreModel):
    user_id = models.ForeignKey(User.uuid)
    contragent_id = models.ForeignKey(Contragent)
