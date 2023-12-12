from rest_framework import serializers

from anri.apps.users.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ("uuid", "company", "name", "phone")
