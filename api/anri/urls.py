"""
URL configuration for anri project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

API_PREFIX = "api"
API_V1_PREFIX = f"{API_PREFIX}/v1"


admin_urlpatterns = [
    path("admin/", admin.site.urls),
]

api_v1_urlpatterns = [
    path(
        f"{API_V1_PREFIX}/",
        include(("anri.apps.products.urls", "products"), namespace="api-v1-products"),
    ),
    path(
        f"{API_V1_PREFIX}/",
        include(("anri.apps.orders.urls", "carts"), namespace="api-v1-carts"),
    ),
    path(
        f"{API_V1_PREFIX}/",
        include(("anri.apps.users.urls", "users"), namespace="api-v1-users"),
    ),
    path(f"{API_V1_PREFIX}/auth/", include("djoser.urls")),
    path(f"{API_V1_PREFIX}/auth/", include("djoser.urls.jwt")),
]

urlpatterns = admin_urlpatterns + api_v1_urlpatterns

if "SWAGGER" in settings.ANRI_FEATURES:
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

    swagger_urlpatterns = [
        path(f"{API_V1_PREFIX}/schema/", SpectacularAPIView.as_view(), name="schema"),
        path(f"{API_V1_PREFIX}/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        path(f"{API_V1_PREFIX}/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
