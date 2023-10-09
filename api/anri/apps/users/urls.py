from rest_framework import routers

from .views import GuestUserViewSet


router = routers.SimpleRouter()
router.register(r"guests", GuestUserViewSet, basename="guest")

urlpatterns = router.urls
