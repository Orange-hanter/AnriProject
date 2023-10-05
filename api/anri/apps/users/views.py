import uuid

from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User

from anri.enviroment import env


class AnonymousUserViewSet(ViewSet):
    @action(detail=False, methods=["post"])
    def create_anonymous_user(self, request):
        """
        Creates an anonymous user in the database and logins as that user.
        Returns jwt-token.
        """

        username_uuid = uuid.uuid4()
        password = env.str("ANRI_ANONYMOUS_USER_PASSWORD")
        email = env.str("ANRI_ANONYMOUS_USER_EMAIL")
        user = User.objects.create_user(username=username_uuid, email=email, password=password)

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )

    @action(detail=False, methods=["post"])
    def is_user_anonymous(self, request):
        return Response(self.request.user.is_anonymous)
