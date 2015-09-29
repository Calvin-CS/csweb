'''
This module defines the features required to support WTforms.

Created on Jul 8, 2014

@author: kvlinden
'''
from flask_wtf.form import Form
from wtforms.fields.simple import SubmitField


class UnitForm(Form):
    '''All information units share these WTforms features for use in editing
    and creating information units.
    '''
    action = None
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')

    # WTForms classes do not (and should not?) have __init__ methods.
    # This was an issue with the Users/Login form and my be relevant to the
    # other information unit classes as well.

    # Don't use the field name 'content', it messes up the HTML/CSS formatting.

    def initialize(self, action=None):
        '''This function initializes the form behavior. Sub-classes should
        specialize this function to populate the form appropriately.
        '''
        self.action = action
        # Set the name of the form action button as appropriate.
        if action == 'edit':
            self.submit.label.text = 'Update'
        elif action == 'create':
            self.submit.label.text = 'Create'
