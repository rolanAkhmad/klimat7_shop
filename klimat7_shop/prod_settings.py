from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-efe_$d2&k5)$pfqgykj&rlaso&jasdnas&=un7!68%m##5rq1ixv^z@s7l*c^+^'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '78.40.109.163', 'klimat7-shop.kz', '*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'klimat7_shop',
        'USER': 'z00sharp',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


STATICFILES_DIRS = [
    Path(BASE_DIR / 'static'),
    Path(BASE_DIR / 'store/static'),
    Path(BASE_DIR / 'core/static'),
    Path(BASE_DIR / 'cart/static'),
    Path(BASE_DIR / 'userprofiles/static'),
]