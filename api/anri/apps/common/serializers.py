from djoser.serializers import UserCreateSerializer

from anri.enviroment import env


class CustomUserCreateSerializer(UserCreateSerializer):
    def save(self, **kwargs):
        if self.context["request"].user.email == env.str("ANRI_GUEST_USER_EMAIL"):
            user = self.context["request"].user
            user.is_active = False
            user.save(update_fields=("is_active",))
            self.instance = user
        return super().save(**kwargs)
