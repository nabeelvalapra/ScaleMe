from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(ROOT_DIR, 'db.sqlite3'),
    }
}
