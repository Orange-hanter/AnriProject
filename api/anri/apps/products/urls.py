from rest_framework import routers

from .views import ProductViewSet, TagViewSet


router = routers.SimpleRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"tags", TagViewSet)

urlpatterns = router.urls
