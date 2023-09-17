from django.db import models

from anri.apps.common.models import CoreModel


class Tag(CoreModel):
    tag_name = models.CharField(max_length=127)
