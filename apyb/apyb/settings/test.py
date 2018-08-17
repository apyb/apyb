import os

TESTING = 'test' in os.sys.argv

if TESTING:
    DEBUG = True

    SECRET_KEY = 'secret-key'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
