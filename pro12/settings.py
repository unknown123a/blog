

from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PORT = os.getenv("PORT", "8080")  # Ensure this matches Railway's port



load_dotenv()



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hawkv4rip-vprk9lerpki*@5ux*#3ds-i=7kyt#p7h&6#7tmi7'


DEBUG = True


# ALLOWED_HOSTS = ['blog-production-7060.up.railway.app','https://blog-production-7060.up.railway.app', "127.0.0.1", "localhost"]
# ALLOWED_HOST =['*']

ALLOWED_HOSTS = [
    os.getenv("RAILWAY_PUBLIC_DOMAIN", "blog-production-7060.up.railway.app"),
    "localhost",
    "127.0.0.1",
    "*"
]


CSRF_TRUSTED_ORIGINS = ['https://blog-production-7060.up.railway.app']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1.apps.App1Config',
    'cloudinary',
    'cloudinary_storage',
    'django_recaptcha',
    'whitenoise.runserver_nostatic',   
    

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





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME' : 'railway',#database name
        'USER':'postgres', #username 
        'PASSWORD':os.environ['DB_PASSWORD'],

        'HOST':'metro.proxy.rlwy.net',
        'PORT':'58564',

    }
}
print(f"Database Name: {DATABASES['default']['NAME']}")
print(f"Database User: {DATABASES['default']['USER']}") 
print(f"Database Host: {DATABASES['default']['HOST']}")
print(f"Database Port: {DATABASES['default']['PORT']}")
print(f"Database Password: {DATABASES['default']['PASSWORD']}")



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



STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'app1' / 'static'  # Your app's static files
]

STATIC_ROOT = BASE_DIR / 'staticfiles'  # Store collected static files centrally
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




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
