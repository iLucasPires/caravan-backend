from environ import Env
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
###############################################################################
# Environment
###############################################################################
env = Env()
env.read_env(
    env_file=BASE_DIR / ".env",
    overwrite=True,
    overrides=True,
    encoding="utf8",
)

DEBUG = env("DJANGO_DEBUG")
SECRET_KEY = env("DJANGO_SECRET_KEY")

###############################################################################
# Network
###############################################################################
ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS", cast=list)

CORS_ALLOWED_ORIGINS = env("DJANGO_CORS_ALLOWED_ORIGINS", cast=list)

CSRF_TRUSTED_ORIGINS = env("DJANGO_CSRF_TRUSTED_ORIGINS", cast=list)

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
}

###############################################################################
# Internationalization
###############################################################################
LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = True

###############################################################################
# Application
###############################################################################
LOCAL_APPS = [
    "app.domain.caravan",
    "app.domain.event",
    "app.domain.payment",
    "app.domain.user",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "drf_spectacular",
    "corsheaders",
    "rest_framework_simplejwt",
    "djoser",
]

INSTALLED_APPS = [
    *DJANGO_APPS,
    *LOCAL_APPS,
    *THIRD_PARTY_APPS,
]

###############################################################################
# Middleware
###############################################################################
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

###############################################################################
# Template
###############################################################################
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": ["django.templatetags.static"],
        },
    },
]


################################################################################
# Database
###############################################################################s
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_POST"),
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

###############################################################################
# Cache
###############################################################################
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": env("REDIS_URL"),
    }
}

###############################################################################
# Task
###############################################################################
TASKS = {
    "default": {
        "BACKEND": "django.tasks.backends.dummy.DummyBackend",
    }
}

###############################################################################
# Storage
###############################################################################
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "access_key": env("S3_ROOT_USER"),
            "secret_key": env("S3_ROOT_PASSWORD"),
            "endpoint_url": env("S3_URL"),
            "bucket_name": env("S3_BUCKET_NAME"),
            "signature_version": "s3v4",
        },
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

###############################################################################
# Static
###############################################################################
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / ".dist"


###############################################################################
# DRF
###############################################################################
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "API",
    "DESCRIPTION": "API",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SCHEMA_PATH_PREFIX": "/api",
}
