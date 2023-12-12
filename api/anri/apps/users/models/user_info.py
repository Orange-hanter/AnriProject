from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

from anri.apps.common.models import CoreModel


class UserInfo(CoreModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.CharField(max_length=128, null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    name = models.CharField(max_length=128)
    phone = PhoneNumberField()
