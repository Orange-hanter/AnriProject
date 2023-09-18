from django.db import models

# from anri.apps.products.models.tags import Tag
from anri.apps.common.models import CoreModel


class ProductTag(CoreModel):
    product = models.ForeignKey("Product")
    # tag_id = models.ForeignKey("Tag")
