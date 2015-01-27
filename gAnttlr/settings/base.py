"""
Django settings for gAnttlr project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'gantt_charts', 'templates', 'gantt_charts'),]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),
                    ]
DB_LOCATION = os.path.join(BASE_DIR, 'gAnttlr', 'db.sqlite3')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lf=9@m6hwa)v-_yf#$8g9^svv&!z$_e5spv-md&o5(y@m_d7^m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}

# import logging
# if DEBUG:
#     # will output to your console
#     logging.basicConfig(
#         level = logging.DEBUG,
#         format = '%(asctime)s %(levelname)s %(message)s',
#     )

# Application definition

PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'toastmessage',
    'lettuce.django',
    'rest_framework',
    'django_extensions',
]

PROJECT_APPS = [
    'gantt_charts',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gAnttlr.urls'

WSGI_APPLICATION = 'gAnttlr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DB_LOCATION,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/'
