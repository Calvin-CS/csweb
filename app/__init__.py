'''
This app package constructor provides a Flask application factory that
initializes the Flask app, the mail instance and the Mongo database based
on a given configuration.

The approach used to deal with the pymongo instance was suggested here:
    http://librelist.com/browser//flask/2013/8/21/flask-pymongo-and-blueprint/#7457e46c374812f8b813185f8692b6b3

The approach to the blueprint and mail instances were suggested by
Miguel Grinberg:
    http://books.google.com/books?id=VKRwAwAAQBAJ&pg=PA78&lpg=PA78&dq=flask+blueprint+factory+flask-mail&source=bl&ots=TOhkN1rR8l&sig=Mcj6qHa6BxZJ4pMBcZTXe0uTpQc&hl=en&sa=X&ei=kKjFU4a1HJSlyASm-IDwBQ&ved=0CCwQ6AEwAjgK#v=onepage&q=flask%20blueprint%20factory%20flask-mail&f=false

Created on Jan 25, 2014
Updated July 16, 2014

@author: kvlinden
'''
from flask.app import Flask
from flask.blueprints import Blueprint
from flask.globals import g
from flask_mail import Mail
from flask_pymongo import PyMongo

from utils.db import db_reset

mail = Mail()


def app_factory(config):
    '''This factory creates a Flask application instance based on the settings
    in the provided configuration object.'''

    # Create the Flask app, register the blueprint and initialize the
    #     flask-mail service.
    # Blueprints must be used to implement factories (I believe) because
    #     they allow the factory to register the application's routes
    #     before they must be implemented.
    app = Flask(__name__)
    app.config.from_object(config)

    from app.views import web
    app.register_blueprint(web)

    mail.init_app(app)

    # Create the (only) mongodb instance for use by all running applications.
    # Different apps may use different Mongo databases.
    # The production server already has its data, so don't always
    #     call db_reset().
    mongo = PyMongo(app)
    if config.DATA:
        with app.app_context():
            db_reset(mongo, config.DATA)

    # Store the Mongo database object in the Flask globals so that it can
    # be accessed when needed.
    @app.before_request
    def before_request():
        g.mongo = mongo

    # This Jinja2 template must be defined here, on the app, rather than
    # in views.py on the blueprint.
    @app.template_filter('start_token')
    def start_token(name):
        '''This routine returns the substring of the given name up to but not
        including the first slash. If there is no slash, it returns the
        full name. It is used in the templates to find either the page
        name or category.'''
        if (name.find('/') == -1):
            return name
        else:
            return name[:name.find('/')]

    return app
