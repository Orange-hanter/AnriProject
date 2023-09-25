from django.db import models

from anri.apps.common.models import CoreModel


class Contragent(CoreModel):
    company_name = models.CharField(max_length=127)
    state_cadastr_address = models.CharField(max_length=127)
    legal_address = models.CharField(max_length=127)
    company_rating = models.DecimalField(max_digits=5, decimal_places=2)
    contact_name = models.CharField(max_length=127)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=31)
