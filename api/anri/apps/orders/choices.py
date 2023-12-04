from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatus(models.TextChoices):
    FORMATION = "FORMATION", _("Formation")
    PAYMENT_WAITING = "PAYMENT WAITING", _("Payment waiting")
    DISPATCH_WAITING = "DISPATCH WAITING", _("Dispatch waiting")
    SENT = "SENT", _("Sent")
    SHIPPED = "SHIPPED", _("Shipped")
    EMERGENCY = "EMERGENCY", _("Emergency")


class PaymentMethod(models.TextChoices):
    ONLINE = "ONLINE", _("Online")
    ON_RECEIPT = "ON_RECEIPT", _("On receipt")
