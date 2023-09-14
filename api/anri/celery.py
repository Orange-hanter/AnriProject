import os

from celery import Celery
from django.core.checks import Error, register

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "anri.settings")

app = Celery("anri")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


@register()
def celery_conf_check(app_configs, **kwargs):
    from django.conf import settings

    mapping_settings = {
        "broker_url": "CELERY_BROKER_URL",
        "task_always_eager": "CELERY_ALWAYS_EAGER",
        "result_backend": "CELERY_RESULT_BACKEND",
        "timezone": "CELERY_TIMEZONE",
        "task_ignore_result": "CELERY_TASK_IGNORE_RESULT",
        "beat_schedule": "CELERYBEAT_SCHEDULE",
    }

    errors = []
    error_index = 0
    for conf_key, setting_key in mapping_settings.items():
        error_index += 1
        if getattr(app.conf, conf_key) != getattr(settings, setting_key):
            errors.append(
                Error(
                    f"Celery conf.{conf_key} not equal settings.{setting_key}",
                    id="celery.E{:03d}".format(error_index),
                )
            )
    return errors
