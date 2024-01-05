from uuid import UUID

from celery import shared_task
from django.db.models import Q

from anri.apps.orders.choices import OrderStatus
from anri.apps.orders.models import Order


@shared_task
def switch_order_status_to_formation(uuid: UUID) -> None:
    Order.objects.filter(Q(uuid=uuid) & Q(status=OrderStatus.PAYMENT_WAITING)).update(status=OrderStatus.FORMATION)
