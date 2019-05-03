# File: ./backend/backend/test_settings.py

from .settings import *  # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'letsstore',
        'USER': 'root',
        'PASSWORD': 'SurukamPass111',
        'HOST': 'localhost'
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'