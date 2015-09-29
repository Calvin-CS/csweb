'''
This module provides the context settings for production, testing and
development.

Created on Jan 1, 2014

@author: kvlinden
'''

import os

from data import dev, test


class Config(object):
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True
    URL = '0.0.0.0'
    # Building a new key on each restart invalidates old sessions but should
    # otherwise work fine.
    SECRET_KEY = os.urandom(24)
    MAIL_SERVER = 'mailhost.calvin.edu'
    MAIL_PORT = 465
    MAIL_USE_SSL = True


class ProductionConfig(Config):
    MONGO_DBNAME = 'csweb'
    # Don't create a database now; the production server uses the production
    # database, which should already be running.
    DATA = None
    # Used as the recipient of contact-us emails...
    MAIL_USERNAME = 'computing@calvin.edu'


class DevelopmentConfig(Config):
    URL = 'localhost'
    MONGO_DBNAME = 'csweb_dev'
    # Note that setting DEBUG to False works with the interactive
    # Eclipse/Pydev debugger; True configures web debug output.
    DEBUG = True
    DATA = dev.data
    # Used as the recipient of contact-us emails...
    MAIL_USERNAME = 'kvlinden@calvin.edu'


class TestingConfig(Config):
    MONGO_DBNAME = 'csweb_test'
    TESTING = True
    # Tests don't work with CSRF turned on, see
    # http://stackoverflow.com/questions/21577481/flask-wtf-wtforms-with-unittest-fails-validation-but-works-without-unittest
    WTF_CSRF_ENABLED = False
    URL = '127.0.0.1'
    DATA = test.data
    # These two TEST_* setting are only used when test discover() is used to
    # collect unit test cases.
    TEST_VERBOSITY = 1
    TEST_DIR = 'test/.'
    # Used as the recipient of test emails...
    MAIL_USERNAME = 'test@test.com'

