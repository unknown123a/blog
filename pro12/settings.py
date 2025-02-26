"""
Django settings for pro12 project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
# wmgz bsfn coww zjer


from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#loat ednv varibake
load_dotenv()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hawkv4rip-vprk9lerpki*@5ux*#3ds-i=7kyt#p7h&6#7tmi7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['blog-production-5107.up.railway.app','https://blog-production-5107.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['blog-production-5107.up.railway.app','https://blog-production-5107.up.railway.app']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',  # Add this before your custom apps
    'app1.apps.App1Config',
    'cloudinary',
    'cloudinary_storage',
    'django_recaptcha',
    

]
AUTH_USER_MODEL =  'app1.CustomUser'

AUTHENTICATION_BACKENDS = [
    'app1.backend.EmailAuthBackend',  # Your custom backend for email authentication
    'django.contrib.auth.backends.ModelBackend',  # The default backend for username-based authentication
]#forthe confiramtion of email using email backend

#email settings
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ='smtp.gmail.com'
EMAIL_FROM ='botcrafty5@gmail.com'
EMAIL_HOST_USER ='botcrafty5@gmail.com'
EMAIL_HOST_PASSWORD ='wmgzbsfncowwzjer'
EMAIL_PORT =587
EMAIL_USE_TLS =True

PASSWORD_RESET_TIMEOUT =14400

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  
]

ROOT_URLCONF = 'pro12.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


WSGI_APPLICATION = 'pro12.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME' : 'railway',#database name
        'USER':'postgres', #username 
        'PASSWORD':'PpvyoydJKKnGDowSlqBemFIogpjMpxqq',
        # 'PASSWORD':os.environ.get('DB_PASSWORD'),

        'HOST':'metro.proxy.rlwy.net',
        'PORT':'58564',

    }
}
# print(os.environ.get('DB_PASSWORD'))  # Debugging the DB_PASSWORD variable



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIR =[
    BASE_DIR / 'static'
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# MEDIA_URL ='media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'app1', 'media')
# MEDIA_URL = 'https://res.cloudinary.com/dc4suo6li/image/upload/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dc4suo6li',
    'API_KEY': '534459399632722',
    'API_SECRET': '92Ina3Dlh_Pw16d--CFDSaQafaY'
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

RECAPTCHA_PUBLIC_KEY = '6LdZLuEqAAAAAGCNY2h_7ZdJ0ZQNnVl7kvo70Z3o'
RECAPTCHA_PRIVATE_KEY = '6LdZLuEqAAAAAJcVcBxWfy8aEfy5Dq4-2xqRXFEf'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django_email.log',  # Logs will be stored here
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
