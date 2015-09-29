'''
To run the production version of this web application, load the csweb
application files onto the production server, copy the csweb application
files into /srv/www/calvin.edu/csweb and then (re)start Nginx, uWSGI and
MongoDB using these control scripts:
    sudo /etc/init.d/mongodb start
    sudo /etc/init.d/nginx start
    sudo /etc/init.d/uwsgi start
The production server will serve webpages up at: http://153.106.116.6 (cs.calvin.edu)

Created on Jan 30, 2013

@author: kvlinden
'''

from app import app_factory
from utils.config import ProductionConfig


config = ProductionConfig()
app = app_factory(config)

if __name__ == "__main__":
    app.run(config.URL)  # Remove the host argument to default to 127.0.0.1.
