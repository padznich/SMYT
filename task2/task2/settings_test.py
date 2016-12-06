from settings import *

DATABASES = {
    "default": dict(
        ENGINE="django.db.backends.sqlite3",
        NAME=":memory:",
    )
}

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
