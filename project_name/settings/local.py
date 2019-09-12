from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', '{{ project_name }}'),
        'USER': os.environ.get('POSTGRES_USER', '{{ project_name }}'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', '{{ project_name }}'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
    }
}