import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kanalservice',
        'USER': 'kanalservice',
        'PASSWORD': 'kanalservice',
        'HOST': 'localhost',
        'PORT': '5432',
        'CONN_MAX_AGE': 60 * 10,  # 10 minutes
    }
}

with open(os.path.join(BASE_DIR, 'kanalservis/secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['localhost', '178.124.179.94', '192.168.1.30', 'alexws.com']

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
