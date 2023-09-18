from django.db import models

from anri.apps.common.models import CoreModel


class ProductPhoto(CoreModel):
    photo_url = models.CharField(max_length=127)
