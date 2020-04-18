import os


class Config(object):
    if 'APP_DEBUG' in os.environ:
        DEBUG = True
    else:
        DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess-this-impossible-secret'
    KMS_KEY_ID = os.getenv('KMS_KEY_ID') or '11521170-712a-46bd-a3d6-1badd43e56c4'
    MEMCACHE_HOST = os.getenv('MEMCACHE_HOST') or 'localhost'
    MEMCACHE_PORT = int(os.getenv('MEMCACHE_PORT')) or 11211
    MEMCACHE_SECRET_LIFESPAN = int(os.getenv('MEMCACHE_SECRET_LIFESPAN')) or 3600
