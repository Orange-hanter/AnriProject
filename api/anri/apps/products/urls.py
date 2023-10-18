from rest_framework import routers

from .views import ProductViewSet, TagViewSet


router = routers.SimpleRouter()
router.register(r"products", ProductViewSet)
router.register(r"tags", TagViewSet)

urlpatterns = router.urls
