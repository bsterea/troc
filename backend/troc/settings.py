from pathlib import Path

# Base directory of the Django backend project.
BASE_DIR = Path(__file__).resolve().parent.parent

# Development secret key.
# This must be replaced with an environment variable before production.
SECRET_KEY = "change-this-secret-key-later"

# Development mode.
# This must be False in production.
DEBUG = True

# Hosts allowed to serve this Django project.
# Empty list is acceptable during local development.
ALLOWED_HOSTS = []

# Installed Django and Troc applications.
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "apps.accounts.apps.AccountsConfig",
    "apps.items.apps.ItemsConfig",
    "apps.exchanges.apps.ExchangesConfig",
    "apps.messaging.apps.MessagingConfig",
    "apps.core.apps.CoreConfig",
]

# Custom user model used by Troc.
# Phone number is the main login identifier.
AUTH_USER_MODEL = "accounts.UserProfile"

# Django middleware stack.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Main URL configuration.
ROOT_URLCONF = "troc.urls"

# Template configuration.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI application entry point.
WSGI_APPLICATION = "troc.wsgi.application"

# Development database.
# SQLite is used for MVP development.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Internationalization settings.
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

# Static files configuration.
STATIC_URL = "static/"

# Media files configuration for uploaded item photos.
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Authentication redirects.
LOGIN_URL = "accounts:login"
LOGIN_REDIRECT_URL = "core:dashboard"
LOGOUT_REDIRECT_URL = "accounts:login"

# END OF FILE
