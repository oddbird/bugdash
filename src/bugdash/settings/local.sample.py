"""
Settings overrides for a particular deployment of this app. The defaults should
be suitable for local development; settings below may need adjustment for a
staging or production deployment.

Copy settings/local.sample.py to settings/local.py and modify as needed.

"""

# Uncomment for a production deployment
#DEBUG = False
#TEMPLATE_DEBUG = False

# This email address will get emailed on 500 server errors.
#ADMINS = [
#    ("Some One", "someone@example.com"),
#]

# Root Bugzilla API URL to use. Defaults to API test sandbox - uncomment to use
# live Mozilla instance.
#BUGZILLA_API_ROOT = "https://api-dev.bugzilla.mozilla.org/1.0"

# Filesystem path to file containing SSL CA certificates necessary to verify
# the server at ``BUGZILLA_API_ROOT`` (if it is an https URL). Defaults to
# GeoTrust Global CA cert currently used for Mozilla Bugzilla instances.
#BUGZILLA_API_SSL_CA_CERT = ""

# Base URL for link to a bug (bug id will be appended). Defaults to API test
# sandbox installation - uncomment to use live Mozilla instance.
#BUGZILLA_BUG_URL_BASE = "https://bugzilla.mozilla.org/show_bug.cgi?id="

# Regular expression for finding deadline and release readiness area in bug
# whiteboard. Defaults to format "[2011-12-15 security]". Regular expression
# must have named groups "deadline" and "area".
#BUGDASH_WHITEBOARD_RE = r"\[(?P<deadline>\d{4}-\d{1,2}-\d{1,2}) (?P<area>[^]]+)\]"

# List of release readiness areas, in rough priority order.
#BUGDASH_AREAS = ["security", "stability", "performance"]

# Absolute path to directory where static assets will be collected by the
# "collectstatic" management command, and can be served by front-end webserver.
# Defaults to absolute filesystem path to "collected-assets/" directory.
#STATIC_ROOT = ""

# Base URL where files in STATIC_ROOT are deployed. Defaults to "/static/".
#STATIC_URL = ""

# A unique (and secret) key for this deployment.
#SECRET_KEY = ""

# Uncomment this (and modify LOCATION appropriately) to use memcached rather
# than local-memory cache. See
# http://docs.djangoproject.com/en/dev/topics/cache/ for more configuration
# options. For faster caching, install pylibmc in place of python-memcached and
# replace MemcachedCache with PyLibMCCache.
#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '127.0.0.1:11211',
#    }
#}

# If a mail server is not available at localhost:25, set these to appropriate
# values:
#EMAIL_HOST = ""
#EMAIL_PORT = ""
# If the mail server configured above requires authentication and/or TLS:
#EMAIL_USE_TLS = True
#EMAIL_HOST_USER = ""
#EMAIL_HOST_PASSWORD = ""
