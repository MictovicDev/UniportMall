"""
Django settings for mictovic project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
#import dj_database_url
import os
from django.conf import settings
# from pyngrok import ngrok

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL = 'authentication.MyUser'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = 'django-insecure-(oawz_u7jb-nih7og2v&rd7=#ag#*&if1xcs@7t_2tmk-1^&#y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#DEBUG = os.environ.get('DEBUG')




ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'authentication',
    'social_django',
    'django_extensions',
    # 'channels',
    'socials',
    'django_celery_beat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    
]
    
#uvicorn mictovic.asgi:application --host 0.0.0.0 --port 8000 --workers 4 --log-level debug


ROOT_URLCONF = 'mictovic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join('BASE_DIR', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]
# WSGI_APPLICATION = 'mictovic.wsgi.application'

# ASGI_APPLICATION = 'mictovic.asgi.application'

ASGI_APPLICATION = 'mictovic.asgi.application'



# CELERY_BROKER_URL = 'redis://localhost:6379'



AUTHENTICATION_BACKENDS = (
                            'social_core.backends.facebook.FacebookOAuth2',
                            'social_core.backends.google.GoogleOAuth2',
                            'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'




# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES["default"] = dj_database_url.parse('postgres://mydb_fs5w_user:igPlWoGZhYIGceDcfNtb4zKbK4Or5St1@dpg-cjeidaunk9qs73bsv96g-a.oregon-postgres.render.com/mydb_fs5w')
SITE_URL = 'example.com:8000/'


SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.8'
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')





SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')



# print(os.environ.get('DBNAME'))

# print(os.environ.get('DB_USER'))
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': 'dTE5ER9IWFPGDRk4wG5l',
#         'HOST': 'containers-us-west-53.railway.app',
#         'PORT': '6789'
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mictovic',
#         'USER': 'postgres',
#         'PASSWORD': 'awa',
#         'HOST': '127.0.0.1',
#         'PORT': '5432'
#     }
# # }

# CHANNEL_LAYERS = {
#     'default':{
#         'BACKEND' : 'channels_redis.core.RedisChannelLayer',
#         'CONFIG' : {
#             'hosts': [('localhost', 6379)]
#         },
#     },
# }


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}

GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')


GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET ')



#GOOGLE_CLIENT_ID = '420280853316-f9rrt3787bvtpuorgehqra0tksh6fqsd.apps.googleusercontent.com'
#GOOGLE_CLIENT_SECRET = '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'

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

if not DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = '587'
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_USER = os.environ.get('EMAIL_HOST_USER')
    SERVER_EMAIL = os.environ.get('EMAIL_HOST_USER')
    BASE_URL = settings.SITE_URL
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
BASE_DIR / 'static',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

print(BASE_DIR)
#python manage.py runserver --port 8000 --noreload --nothreading --no-ipv6 --noreload --asgi mictovic.asgi:application
