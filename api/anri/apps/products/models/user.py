from django.contrib.auth.models import User as user

from anri.apps.common.models import CoreModel


class User(CoreModel, user):
    pass
