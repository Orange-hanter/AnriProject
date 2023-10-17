from anri.enviroment import env

from .django import TIME_ZONE as DJANGO_TIME_ZONE
from celery.schedules import crontab


CELERY_ALWAYS_EAGER = env.bool("ANRI_CELERY_ALWAYS_EAGER", default=False)
CELERY_BROKER_URL = env.str("ANRI_CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env.str("ANRI_CELERY_RESULT_BACKEND_URL", default=CELERY_BROKER_URL)

CELERY_TIMEZONE = DJANGO_TIME_ZONE
CELERY_TASK_IGNORE_RESULT = True

CELERY_BEAT_SCHEDULE = {
    "delete_users": {
        "task": "anri.apps.users.tasks.delete_unverified_users",
        "schedule": crontab(minute=0, hour=0),  # how often task runs
    },
}
