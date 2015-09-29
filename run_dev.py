'''
To run the development version of this web application, start MongoDB
(by running mongodb-path/mongod) and then run this module. The development
server will serve webpages up at: http://localhost:5000/.

Created on Dec 31, 2013

@author: kvlinden
'''

from app import app_factory
from utils.config import DevelopmentConfig


config = DevelopmentConfig()
app = app_factory(config)

if __name__ == '__main__':
    app.run(config.URL)  # Remove the host argument to default to 127.0.0.1.
