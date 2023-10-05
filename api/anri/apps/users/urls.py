from rest_framework import routers

from .views import AnonymousUserViewSet


router = routers.SimpleRouter()
router.register(r"anonymous_users", AnonymousUserViewSet, basename="anonymous_user")

urlpatterns = router.urls
