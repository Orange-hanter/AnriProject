from rest_framework import routers

from .views import OrderViewSet


router = routers.SimpleRouter()
router.register(r"orders", OrderViewSet, basename="order")

urlpatterns = router.urls
