from django.db import models

from anri.apps.products.models.tags import Tag
from anri.apps.products.models.products import Product
from anri.apps.common.models import CoreModel


class ProductTag(CoreModel):
    product_id = models.ForeignKey(Product)
    tag_id = models.ForeignKey(Tag)
