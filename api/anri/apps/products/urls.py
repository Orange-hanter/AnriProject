from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from .views import ProductViewSet, TagViewSet


router = routers.SimpleRouter()
router.register(r"products", ProductViewSet)
router.register(r"tags", TagViewSet)

urlpatterns = router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
