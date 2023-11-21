from celery import shared_task

from anri.apps.orders.models import Order


@shared_task
def delete_order(uuid: str) -> None:
    qs = Order.objects.filter(uuid=uuid).delete()
