SECRET_KEY = "srvm-fixture-only-not-a-real-secret"
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = []
MIDDLEWARE = []
ROOT_URLCONF = "app.urls"
WSGI_APPLICATION = "app.wsgi.application"

# No database is configured on purpose: runserver skips its migration check
# when the default connection raises ImproperlyConfigured.
DATABASES = {}
