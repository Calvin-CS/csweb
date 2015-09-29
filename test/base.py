'''
This class is parent class for all csweb unit tests. It sets up the application and database.

Created on Jan 25, 2014

@author: kvlinden
'''

from flask.blueprints import Blueprint
from flask_mail import Mail
from flask_testing import TestCase

from app import app_factory
from utils.config import TestingConfig


mail = Mail()

class CSWebTestBase(TestCase):
 
    def create_app(self):
        app = app_factory(TestingConfig())
        mail.init_app(app)
        return app    
    
    def setUp(self):
        self.app = self.app.test_client()
    # No tearDown() is required because db_reset() clears and rebuilds the database.
        
