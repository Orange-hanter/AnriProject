from celery import shared_task
from django.contrib.auth.models import User
from datetime import datetime, timedelta

import pytz

from anri.settings import CELERY_TIMEZONE


@shared_task(bind=True)
def delete_unverified_users(self):
    tz = pytz.timezone(CELERY_TIMEZONE)
    users_non_active = User.objects.filter(is_active=False)
    for user in users_non_active:
        if (datetime.now(tz) - user.date_joined) > timedelta(days=2):
            user.delete()
