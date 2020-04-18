import os


class Config(object):
    if 'APP_DEBUG' in os.environ:
        DEBUG = True
    else:
        DEBUG = False
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY') or 'evLQLbtvsvOYnOba8mvbl0k1-k4mim102e109m109m210'
    KMS_KEY_ID = os.getenv('KMS_KEY_ID') or 'EnterValidKeyID'
    MEMCACHE_HOST = os.getenv('MEMCACHE_HOST') or 'localhost'
    MEMCACHE_PORT = int(os.getenv('MEMCACHE_PORT')) or 11211
    MEMCACHE_SECRET_LIFESPAN = int(os.getenv('MEMCACHE_SECRET_LIFESPAN')) or 3600
