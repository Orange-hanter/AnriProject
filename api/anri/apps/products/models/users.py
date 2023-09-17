from django.db import models

from anri.apps.common.models import CoreModel


class User(CoreModel):
    user_name = models.CharField(max_length=127, null=False)
    user_email = models.CharField(max_length=127, null=False)
    password = models.CharField(max_length=127, null=False)
