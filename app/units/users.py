'''
This module defines the features required to support authentication using the
user object(s) in the database and to support the system login form. See
unit.py and unitForm.py for more details.

Created on Jul 11, 2014

@author: kvlinden
'''
from flask.globals import g
from wtforms.fields.simple import TextField, PasswordField

from app.units.unit import Unit
from app.units.unitForm import UnitForm


class Users(Unit, UnitForm):
    '''This class encapsulates tools for users and logins. These are not
    information units, but they come from the database nevertheless.
    '''
    @classmethod
    def read_unit(cls, name):
        return g.mongo.db.users.find_one({'name': name})

    # Specify the WTForms elements.
    name = action = 'login'
    nameField = TextField('Username')
    passwordField = PasswordField('Password')
