from django.db import models

from anri.apps.common.models.core_model import CoreModel


class Tag(CoreModel):
    name = models.CharField(max_length=64)
