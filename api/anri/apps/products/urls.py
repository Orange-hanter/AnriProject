from rest_framework import routers

from .views import ProductListViewSet


router = routers.SimpleRouter()
router.register(r"products", ProductListViewSet)

urlpatterns = router.urls
