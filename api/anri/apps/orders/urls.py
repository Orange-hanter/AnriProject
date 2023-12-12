from rest_framework import routers

from .views import CartViewSet, OrderViewSet


router = routers.SimpleRouter()
router.register(r"carts", CartViewSet, basename="cart")
router.register(r"orders", OrderViewSet, basename="order")

urlpatterns = router.urls
