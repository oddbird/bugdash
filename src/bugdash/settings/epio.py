from .prod import *

from bundle_config import config

COMPRESS_OUTPUT_DIR = "cache"

CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": "{host}:{port}".format(
                host=config["redis"]["host"],
                port=config["redis"]["port"]),
        "OPTIONS": {
            "PASSWORD": config["redis"]["password"],
        },
        "VERSION": config["core"]["version"],
    },
}

SERVER_EMAIL = "server@bugdash.ep.io"
DEFAULT_FROM_EMAIL = "server@bugdash.ep.io"
EMAIL_HOST = "mail.threepines.org"
EMAIL_PORT = "587"
EMAIL_USE_TLS = True

SECURE_SSL_HOST = "bugdash.ep.io"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "SSL")
