REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_RENDER_CLASSES": [
        "rest_framework.renders.JSONRenderer",
        "rest_framework.renders.BrowsableAPIRenderer",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}


# CORS_ALLOWED_ORIGINS = env.list("ANRI_CORS_ALLOWED_ORIGINS", default=[])
# CORS_ALLOW_ALL_ORIGINS = env.bool("ANRI_CORS_ALLOW_ALL_ORIGINS", default=False)
