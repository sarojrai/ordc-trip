# logging dictConfig configuration
import os
#from getenv import env
from doordelvr.settings import DEBUG

min_django_level = 'INFO'


if DEBUG:
    min_level = 'DEBUG'
else:
    min_level = 'INFO'

BASE_DIR = None #env('LOG_PATH')
if not BASE_DIR:
    BASE_DIR = '/tmp'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'timestampthread': {
            'format': "%(asctime)s [%(levelname)-8.8s]   [%(threadName)s %(thread)d] [%(name)s %(filename)s: %(lineno)d]  %(message)s",
            # 'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'fileHandler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename':  os.path.join(BASE_DIR, "doordelvr.log"),  # '/Users/upendra/Desktop/log/debug.log',
            'maxBytes': 10 * 10**6,  # will 10 MB do?
            'backupCount': 10,  # keep this many extra historical files
            'formatter': 'timestampthread'
        },
        'apiFileHandler': {
            'level': min_level,  # this level or higher goes to the log file
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR,  "doordelvr-api.log"),
            'maxBytes': 10 * 10**6,  # will 10 MB do?
            'backupCount': 10,  # keep this many extra historical files
            'formatter': 'timestampthread'
        },
        'djangoFileHandler': {
            # optionally raise to INFO to not fill the log file too quickly
            'level': min_level,  # this level or higher goes to the log file
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR,  "doordelvr-django-file.log"),
            'maxBytes': 10 * 10**6,  # will 10 MB do?
            'backupCount': 10,  # keep this many extra historical files
            'formatter': 'timestampthread'
        },
        'requestFileHandler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename':  os.path.join(BASE_DIR, "doordelvr-request.log"),  # '/Users/upendra/Desktop/log/debug.log',
            'maxBytes': 10 * 10**6,  # will 10 MB do?
            'backupCount': 10,  # keep this many extra historical files
            'formatter': 'timestampthread'
        },
        'dbFileHandler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename':  os.path.join(BASE_DIR, "doordelvr-db.log"),  # '/Users/upendra/Desktop/log/debug.log',
            'maxBytes': 10 * 10**6,  # will 10 MB do?
            'backupCount': 10,  # keep this many extra historical files
            'formatter': 'timestampthread'
        },
        'console': {
            'level': 'DEBUG',
            'filters': [],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mailAdmins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['fileHandler', 'console', 'mailAdmins'],
            'propagate': True,
        },
        'django': {
            'handlers': ['djangoFileHandler', 'mailAdmins'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'api': {
            'handlers': ['apiFileHandler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['requestFileHandler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db': {
            'handlers': ['dbFileHandler'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
