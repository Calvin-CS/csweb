'''
This module defines the features required to support CRUD operations on
documents in the database. The documents are stored in the CMS, not as static
files, which distinguishes them from the files loaded in the /static/department
sub-directory. See unit.py and unitForm.py for more details.

The CMS user is expected to choose unique document names.

Created on Jul 24, 2014

@author: kvlinden
'''
from random import randint

from bson.objectid import ObjectId
from flask.globals import g
from wtforms.fields.simple import TextField, TextAreaField, HiddenField

from app.units.unit import Unit
from app.units.unitForm import UnitForm
from app.utilities import get_today


class Documents(Unit, UnitForm):
    '''This class encapsulates tools for user-created documents.'''

    @classmethod
    def create_unit(cls, form):
        '''This routine creates an document based on the given values.
        The edit date is set to the current date. The unique is set by
        the user, not by the system.'''
        record = {}
        record['name'] = form.nameField.data
        record['title'] = form.titleField.data
        record['content'] = form.contentField.data
        record['date'] = get_today()
        return g.mongo.db.documents.insert(record)

    @classmethod
    def read_unit(cls, name):
        '''This routine find an document with the given nameField.'''
        return g.mongo.db.documents.find_one({'name': name})

    @classmethod
    def read_units(cls):
        '''This routine gets all documents stored in the database.'''
        # find().sort() returns a PyMongo cursor, not a list. Use list() to
        # convert the cursor to a list and, thus, to download all the documents
        # at once. Before reconfiguring the factory, we didn't have to do this
        # for some reason; now we do.
        return list(g.mongo.db.documents.find().sort('name'))

    @classmethod
    def update_unit(cls, form):
        '''This routine sets the database-stored information for the given
        document to the given values. The document is identified by mongo's
        _id rather than the name because the user may have changed the name.
        The edit date is set to the current date.
        '''
        mongoId = ObjectId(form.idField.data)
        document_record = g.mongo.db.documents.find_one({'_id': mongoId})
        if document_record is not None:
            document_record['name'] = form.nameField.data
            document_record['title'] = form.titleField.data
            document_record['content'] = form.contentField.data
            document_record['date'] = get_today()
            g.mongo.db.documents.save(document_record)

    @classmethod
    def delete_unit(cls, name):
        '''This routine deletes the document entry with the given nameField.
        It leaves the actual document in place.
        '''
        return g.mongo.db.documents.remove({'name': name})

    # Specify the WTForms elements.
    idField = HiddenField('_id')
    nameField = TextField('Name')
    titleField = TextField('Title')
    contentField = TextAreaField('Content')

    def initialize(self, name='', action=None, document=None):
        super(Documents, self).initialize(action=action)
        # If there is a document, populate the field values.
        if document:
            if action != 'create':
                self.idField.data = str(document.get('_id'))
            self.nameField.data = document.get('name')
            self.titleField.data = document.get('title')
            self.contentField.data = document.get('content')

    def getName(self):
        '''This method returns the name of document, which is
        useful when the CMS user modifies the document name.'''
        return self.nameField.data
    