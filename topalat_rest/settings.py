"""
Django settings for topalat_rest project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import dj_database_url
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config("SECRET_KEY", default='changeme')

DEBUG = config("DEBUG", default=False, cast=bool)

# ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.43.229']
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # app specific
    'authentication',
    'charge',
    'core',
    'services',
    'support',

    # third party
    'rest_framework',
    'django_filters',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'topalat_rest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'topalat_rest.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'topalatdb',
    #     'USER': 'topalatdbuser',
    #     'PASSWORD': 'secret',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
    # },

    # "default": {
    #     "ENGINE": config("SQL_ENGINE", default="django.db.backends.sqlite3"),
    #     "NAME": config("SQL_DATABASE", default=os.path.join(BASE_DIR, "db.sqlite3")),
    #     "USER": config("SQL_USER", default="user"),
    #     "PASSWORD": config("SQL_PASSWORD", default="password"),
    #     "HOST": config("SQL_HOST", default="localhost"),
    #     "PORT": config("SQL_PORT", default="5432"),
    # }
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'core.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ),

    'DEFAULT_PAGINATION_CLASS':
        'core.pagination.LimitOffsetPaginationWithMaxLimit',

    'PAGE_SIZE': 100,

    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10000/hour',
        'user': '20000/hour',
        'stories': '30000/hour',

    }

}

SIMPLE_JWT = {
    # 'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
    # 'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    #
    'ACCESS_TOKEN_LIFETIME': timedelta(weeks=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(weeks=2),
}

AUTH_USER_MODEL = 'authentication.User'

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = [
#     # 'http://google.com',
#     # 'http://hostname.example.com',
#     'http://localhost:8000',
#     'http://localhost:3000',
#     'http://localhost:3001',
#     'http://127.0.0.1:8000'
# ]

CORS_ALLOW_CREDENTIALS = True

# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'parsifal_app'
# EMAIL_HOST_PASSWORD = 'mys3cr3tp4ssw0rd'
# EMAIL_USE_TLS = True

###############
# EMAIL SETUP #
###############
EMAIL_HOST = config("EMAIL_HOST", default='smtp.gmail.com')
EMAIL_PORT = config("EMAIL_PORT", default=587, cast=int)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True, cast=bool)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default='topalatonline@gmail.com')
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default='12345678=Aa')
EMAIL_BACKEND = config("EMAIL_BACKEND", default='django.core.mail.backends.smtp.EmailBackend')

########################
# OTHER EMAIL SETTINGS #
# https://www.geeksforgeeks.org/setup-sending-email-in-django-project/ #
########################
ADMIN_EMAIL = config("ADMIN_EMAIL", default="topalatonline@gmail.com")
SUPPORT_EMAIL = config("SUPPORT_EMAIL", default="topalatonline@gmail.com")
DEFAULT_FROM_EMAIL = ADMIN_EMAIL
SERVER_EMAIL = ADMIN_EMAIL
