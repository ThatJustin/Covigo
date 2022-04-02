"""
Django settings for Covigo project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import json

from dotenv import load_dotenv
from pathlib import Path
from os import getenv

# Load variables from .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


# Configure settings based on "dev mode" or "production mode"
PRODUCTION_MODE = getenv("PRODUCTION_MODE") == "True"

if PRODUCTION_MODE:
    DEBUG = False
    ALLOWED_HOSTS = json.loads(getenv("ALLOWED_HOSTS"))
    STATIC_ROOT = getenv("STATIC_ROOT")
    SECRET_KEY = getenv("SECRET_KEY")
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    HOST_NAME = 'https://covigo.ddns.net'
    STATICFILES_DIRS = [BASE_DIR / 'static', ]
else:
    try:
        ALLOWED_HOSTS = json.loads(getenv("ALLOWED_HOSTS"))
    except TypeError:
        ALLOWED_HOSTS = []
    DEBUG = True
    SECRET_KEY = 'django-insecure-)hrxs16w-%lr2@k@!rfq!lwem55i%uv$7qhiktrme63j!2+1(f'
    HOST_NAME = 'http://localhost:8000'

# Application definition

INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',
    'manager.apps.ManagerConfig',
    'dashboard.apps.DashboardConfig',
    'status.apps.StatusConfig',
    'appointments.apps.AppointmentsConfig',
    'messaging.apps.MessagingConfig',
    'symptoms.apps.SymptomsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'django_user_agents',
    'two_factor',
    'users'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'Covigo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Covigo.context_processors.production_mode',
            ],
        },
    },
]

WSGI_APPLICATION = 'Covigo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASE_PASSWORD = getenv("DATABASE_PASSWORD")

if getenv("DATABASE_USER"):
    DATABASE_USER = getenv("DATABASE_USER")
else:
    DATABASE_USER = 'root'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Covigo',
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'
DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'
L10N = False

USE_I18N = False

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/accounts/two_factor_authentication'
LOGOUT_REDIRECT_URL = '/accounts/login'
