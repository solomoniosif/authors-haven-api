from .base import *
from .base import env


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default='django-insecure-b#i9gm_m+*53*g^l9bj60v&2c95qk)^he!oe6#%m$*i%b%p#la')


ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']
