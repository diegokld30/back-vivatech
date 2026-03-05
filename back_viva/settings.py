"""
Django settings for back_viva project (desarrollo local)
"""

from pathlib import Path
import datetime
import environ

# ────────────────────────────────────────────────────────────
# Rutas y entorno
# ────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "change-me"),
    ALLOWED_HOSTS=(str, ""),
    DATABASE_URL=(str, f"sqlite:///{BASE_DIR/'db.sqlite3'}"),
    CORS_ALLOW_ALL_ORIGINS=(bool, False),
    SECURE_SSL_REDIRECT=(bool, False),
    SESSION_COOKIE_SECURE=(bool, True),
    CSRF_COOKIE_SECURE=(bool, True),
    SECURE_HSTS_SECONDS=(int, 31536000),
    SECURE_HSTS_INCLUDE_SUBDOMAINS=(bool, True),
    SECURE_HSTS_PRELOAD=(bool, True),
    SECURE_PROXY_SSL_HEADER=(str, "HTTP_X_FORWARDED_PROTO,https"),
    USE_X_FORWARDED_HOST=(bool, True),
)

# Cargar .env si existe
environ.Env.read_env(BASE_DIR / ".env")

DEBUG = env.bool("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(",") if env("ALLOWED_HOSTS") else ["*"]
CORS_ALLOWED_ORIGINS = (
    env("CORS_ALLOWED_ORIGINS").split(",")
    if env("CORS_ALLOWED_ORIGINS")
    else []
)
CORS_ALLOW_ALL_ORIGINS = env.bool("CORS_ALLOW_ALL_ORIGINS")
CSRF_TRUSTED_ORIGINS = (
    env("CSRF_TRUSTED_ORIGINS").split(",")
    if env("CSRF_TRUSTED_ORIGINS")
    else []
)
# ────────────────────────────────────────────────────────────
# Aplicaciones
# ────────────────────────────────────────────────────────────
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY = [
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
]

LOCAL_APPS = [
    "apps.catalog",
    "apps.clients",
    "apps.blog",
    "apps.core",
    "apps.about",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY + LOCAL_APPS
INSTALLED_APPS += ["corsheaders", "ckeditor", "django_json_widget"]

# ────────────────────────────────────────────────────────────
# Middleware y BASICS
# ────────────────────────────────────────────────────────────
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "back_viva.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "back_viva.wsgi.application"

# ────────────────────────────────────────────────────────────
# Base de datos
# ────────────────────────────────────────────────────────────
DATABASES = {"default": env.db("DATABASE_URL")}

# ────────────────────────────────────────────────────────────
# Passwords
# ────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ────────────────────────────────────────────────────────────
# Internacionalización
# ────────────────────────────────────────────────────────────
LANGUAGE_CODE = "es-co"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True

# ────────────────────────────────────────────────────────────
# Static & Media (desarrollo local)
# ────────────────────────────────────────────────────────────
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ────────────────────────────────────────────────────────────
# Django REST Framework + JWT
# ────────────────────────────────────────────────────────────
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(hours=4),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# ────────────────────────────────────────────────────────────
# drf-spectacular
# ────────────────────────────────────────────────────────────
SPECTACULAR_SETTINGS = {
    "TITLE": "Vivatech API",
    "DESCRIPTION": "Catálogo de productos, clientes y blog",
    "VERSION": "0.1.0",
}

# ────────────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CKEditor Settings
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
    },
}

# Seguridad detrás de proxy reverso (Nginx/LB)
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT")
SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE")
CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE")
SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS")
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("SECURE_HSTS_INCLUDE_SUBDOMAINS")
SECURE_HSTS_PRELOAD = env.bool("SECURE_HSTS_PRELOAD")
USE_X_FORWARDED_HOST = env.bool("USE_X_FORWARDED_HOST")
_secure_proxy_ssl_header = env("SECURE_PROXY_SSL_HEADER")
if _secure_proxy_ssl_header and "," in _secure_proxy_ssl_header:
    _header_name, _header_value = [part.strip() for part in _secure_proxy_ssl_header.split(",", 1)]
    SECURE_PROXY_SSL_HEADER = (_header_name, _header_value)
