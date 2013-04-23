from .base import *

ROOT_URLCONF = 'gsgisng.urls.development'

STATIC_ROOT = PROJECT_DIR.child('static')
MEDIA_ROOT = PROJECT_DIR.child('media')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'gsgisng@gmail.com'
EMAIL_HOST_PASSWORD = 'ciaociaociao'

INSTALLED_APPS = INSTALLED_APPS + (
    'pybab',
    'pybab.api',
    'pyhive.extra.django',
    'gswebgis.setup',
    'plrutils',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'ERROR',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'raven': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

