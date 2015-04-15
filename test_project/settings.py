

import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

try:
    import django.test.runner
    TEST_RUNNER = "django.test.runner.DiscoverRunner"
except ImportError as e:
    TEST_RUNNER = "django.test.simple.DjangoTestSuiteRunner"

SECRET_KEY = "hi mom"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db',
    }
}

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

INSTALLED_APPS = (
    'overextends',
)

