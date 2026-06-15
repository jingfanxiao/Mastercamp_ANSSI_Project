from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = BASE_DIR.parent

SECRET_KEY = 'django-insecure-anssi-cve-dashboard-change-in-production'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'anssi_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'anssi_project.wsgi.application'

LANGUAGE_CODE = 'fr-fr'
USE_I18N = False

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    ('plots', PROJECT_ROOT / 'outputs' / 'plots'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
