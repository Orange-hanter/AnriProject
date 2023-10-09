from djoser.serializers import UserCreateSerializer
from django.contrib.auth.models import User

from anri.enviroment import env


class CustomUserCreateSerializer(UserCreateSerializer):
    def save(self, **kwargs):
        if self.context["request"].user.email == env.str("ANRI_GUEST_USER_EMAIL"):
            user = User.objects.filter(pk=self.context["request"].user.id)
            user.is_active = False
            user.save()
            self.instance = user
        return super().save(**kwargs)
