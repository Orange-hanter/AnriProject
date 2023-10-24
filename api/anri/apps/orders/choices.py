from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatus(models.TextChoices):
    FORMATION = "FORMATION", _("Formation")
    PAYMENT_WAITING = "PAYMENT WAITING", _("Payment Waiting")
    DISPATCH_WAITING = "DISPATCH WAITING", _("Dispatch Waiting")
    SENT = "SENT", _("Sent")
    SHIPPED = "SHIPPED", _("Shipped")
    EMERGENCY = "EMERGENCY", _("Emergency")
