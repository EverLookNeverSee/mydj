"""
Django settings for mydj project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-chh$&6-#98z$ftso4$qu1-zw0%h&ebxfo+&a!2ae0q+8z1a%iv'

# Application definition

INSTALLED_APPS = [
    "multi_captcha_admin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "website",
    "blog",
    "accounts",
    "django.contrib.humanize",
    "django_extensions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "robots",
    "debug_toolbar",
    "taggit",
    "django_summernote",
    "captcha",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'mydj.urls'

ROBOTS_USE_HOST = True
ROBOTS_USE_SITEMAP = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mydj.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = "/media/"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    "127.0.0.1"
]

# summernote configs
X_FRAME_OPTIONS = "SAMEORIGIN"
SUMMERNOTE_THEME = "bs4"
SUMMERNOTE_CONFIG = {
    "iframe": True,
    "width": "100%",
    "height": "480",
    "toolbar": [
        ["style", ["style"]],
        ["font", ["bold", "italic", "underline", "clear"]],
        ["fontname", ["fontname"]],
        ["color", ["color"]],
        ["paragraph", ["ul", "ol", "paragraph"]],
        ["height", ["height"]],
        ["table", ["table"]],
        ["insert", ["link", "picture", "video"]],
        ["view", ["fullscreen", "codeview"]],
    ],
}


# captcha admin settings
MULTI_CAPTCHA_ADMIN = {
    "engine": "simple-captcha",
}

# Authentication Backends
AUTHENTICATION_BACKENDS = ["accounts.backends.EmailBackend"]


# email configs
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'EverLookNeverSee@outlook.com'  # str(os.getenv())
EMAIL_HOST_PASSWORD = 'C''g@(:R9P)_K,U'  # str(os.getenv())
