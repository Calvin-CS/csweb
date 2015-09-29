'''
This module defines the features required to support CRUD operations on
resources in the database. See unit.py and unitForm.py for more details.

The CMS user is expected to choose unique resource names.

This is pretty much a copy of the the documents unit, designed to represent
department resources (linked from the main menu) separately from department
documents (linked from other content pages). Resources can only be created
and deleted by the webmaster; CMS users can only view and update them. The
resources are ordered using a numeric ordinal field, which is required,
presumably, because Mongo orders collections whose elements have differing
fields in non-definition order.

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


class Resources(Unit, UnitForm):
    '''This class encapsulates tools for user-created resources.'''

#     @classmethod
#     def create_unit(cls, form):
#         '''This routine creates a resource based on the given values.
#         The edit date is set to the current date. The unique is set by
#         the user, not by the system.'''
#         record = {}
#         record['name'] = form.nameField.data
#         record['ordinal'] = form.ordinalField.data
#         record['title'] = form.titleField.data
#         record['summary'] = form.summaryField.data
#         record['content'] = form.contentField.data
#         record['date'] = get_today()
#         return g.mongo.db.resources.insert(record)

    @classmethod
    def read_unit(cls, name):
        '''This routine find an resource with the given nameField.'''
        return g.mongo.db.resources.find_one({'name': name})

    @classmethod
    def read_units(cls):
        '''This routine gets all resources stored in the database.'''
        return list(g.mongo.db.resources.find().sort('ordinal'))

    @classmethod
    def update_unit(cls, form):
        '''This routine sets the database-stored information for the given
        resource to the given values. The resource is identified by mongo's
        _id rather than the name because the user may have changed the name.
        The edit date is set to the current date.
        '''
        mongoId = ObjectId(form.idField.data)
        resource_record = g.mongo.db.resources.find_one({'_id': mongoId})
        if resource_record is not None:
            resource_record['name'] = form.nameField.data
            resource_record['ordinal'] = form.ordinalField.data
            resource_record['title'] = form.titleField.data
            resource_record['summary'] = form.summaryField.data
            resource_record['content'] = form.contentField.data
            resource_record['contentTab1Title'] = form.contentTab1TitleField.data
            resource_record['contentTab1'] = form.contentTab1Field.data
            resource_record['contentTab2Title'] = form.contentTab2TitleField.data
            resource_record['contentTab2'] = form.contentTab2Field.data
            resource_record['contentTab3Title'] = form.contentTab3TitleField.data
            resource_record['contentTab3'] = form.contentTab3Field.data
            resource_record['date'] = get_today()
            g.mongo.db.resources.save(resource_record)

#     @classmethod
#     def delete_unit(cls, name):
#         '''This routine deletes the resource entry with the given nameField.
#         It leaves the actual resource in place.
#         '''
#         return g.mongo.db.resources.remove({'name': name})

    # Specify the WTForms elements.
    idField = HiddenField('_id')
    nameField = TextField('Name')
    ordinalField = TextField('Ordinal')
    titleField = TextField('Title')
    summaryField = TextField('Summary')
    contentField = TextAreaField('Content')
    contentTab1TitleField = TextField('Content Tab1 Title')
    contentTab1Field = TextAreaField('Content Tab1')
    contentTab2TitleField = TextField('Content Tab2 Title')
    contentTab2Field = TextAreaField('Content Tab2')
    contentTab3TitleField = TextField('Content Tab3 Title')
    contentTab3Field = TextAreaField('Content Tab3')

    def initialize(self, name='', action=None, resource=None):
        super(Resources, self).initialize(action=action)
        # If there is a resource, populate the field values.
        if resource:
            if action != 'create':
                self.idField.data = str(resource.get('_id'))
            self.nameField.data = resource.get('name')
            self.ordinalField.data = resource.get('ordinal')
            self.titleField.data = resource.get('title')
            self.summaryField.data = resource.get('summary')
            self.contentField.data = resource.get('content')
            self.contentTab1TitleField.data = resource.get('contentTab1Title')
            self.contentTab1Field.data = resource.get('contentTab1')
            self.contentTab2TitleField.data = resource.get('contentTab2Title')
            self.contentTab2Field.data = resource.get('contentTab2')
            self.contentTab3TitleField.data = resource.get('contentTab3Title')
            self.contentTab3Field.data = resource.get('contentTab3')

    def getName(self):
        '''This method returns the name of resource, which is
        useful when the CMS user modifies the resource name.'''
        return self.nameField.data
    