from rest_framework import routers

from .views import CartViewSet


router = routers.SimpleRouter()
router.register(r"carts", CartViewSet, basename="cart")

urlpatterns = router.urls
