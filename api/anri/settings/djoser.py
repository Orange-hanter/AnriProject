from anri.enviroment import env


EMAIL_USE_TLS = True
EMAIL_HOST = env.str("ANRI_EMAIL_HOST")
EMAIL_PORT = env.str("ANRI_EMAIL_PORT")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST_USER = env.str("ANRI_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env.str("ANRI_EMAIL_HOST_PASSWORD")


DJOSER = {
    "USER_ID_FIELD": "username",
    "LOGIN_FIELD": "email",
    "SEND_ACTIVATION_EMAIL": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "ACTIVATION_URL": "activation/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "username-reset/{uid}/{token}",
    "SERIALIZERS": {
        "activation": "djoser.serializers.ActivationSerializer",
        "password_reset": "djoser.serializers.SendEmailResetSerializer",
        "password_reset_confirm": "djoser.serializers.PasswordResetConfirmSerializer",
        "password_reset_confirm_retype": "djoser.serializers.PasswordResetConfirmRetypeSerializer",
        "set_password": "djoser.serializers.SetPasswordSerializer",
        "set_username": "djoser.serializers.SetUsernameSerializer",
        "username_reset": "djoser.serializers.SendEmailResetSerializer",
        "username_reset_confirm": "djoser.serializers.UsernameResetConfirmSerializer",
        "user_create": "djoser.serializers.UserCreateSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
        "user": "djoser.serializers.UserSerializer",
        "current_user": "djoser.serializers.UserSerializer",
    },
    "EMAIL": {
        "activation": "anri.apps.users.email.ActivationEmail",
        "confirmation": "anri.apps.users.email.ConfirmationEmail",
        "password_reset": "djoser.email.PasswordResetEmail",
        "password_changed_confirmation": "djoser.email.PasswordChangedConfirmationEmail",
        "username_changed_confirmation": "djoser.email.UsernameChangedConfirmationEmail",
        "username_reset": "djoser.email.UsernameResetEmail",
    },
}

SITE_NAME = "AnriDecor"
