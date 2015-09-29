'''
This module defines the features required to support CRUD operations on images
in the database. The image files are stored as static content; the database
stores meta-information on them (e.g., URL, description, tags). Note
tags are represented as lists of symbols. See unit.py and unitForm.py for more
details.

The CMS user is expected to choose unique image names.

Created on Jul 23, 2014

@author: kvlinden
'''
from random import randint

from bson.objectid import ObjectId
from flask.globals import g
from wtforms.fields.simple import TextField, HiddenField

from app.units.unit import Unit
from app.units.unitForm import UnitForm
from app.utilities import get_today


class Images(Unit, UnitForm):
    '''This class encapsulates tools for images.'''

    @classmethod
    def create_unit(cls, form):
        '''This routine creates an image based on the given values.
        The edit date is set to the current date.'''
        record = {}
        record['name'] = form.nameField.data
        record['filename'] = form.filenameField.data
        record['description'] = form.descriptionField.data
        record['tags'] = form.tagsField.data.split(', ')
        record['date'] = get_today()
        g.mongo.db.images.insert(record)
        return record['name']

    @classmethod
    def read_unit(cls, name):
        '''This routine find an image with the given nameField.'''
        return g.mongo.db.images.find_one({'name': name})

    @classmethod
    def read_tagged_unit(cls, tag):
        '''This routine finds an image with the given tag. It returns None if
        there are no tagsField or if there are no matching images, and it
        returns a random image if more than one image matches the tag.
        '''
        if tag is None:
            return None
        image_records = list(g.mongo.db.images.find({'tags': tag}))
        if image_records and (len(image_records) > 0):
            image = image_records[randint(0, len(image_records) - 1)]
            return image
        else:
            return None

    @classmethod
    def read_units(cls):
        '''This routine gets all images stored in the database, sorted by
        nameField.
        '''
        # find().sort() returns a PyMongo cursor, not a list. Use list() to
        # convert the cursor to a list and, thus, to download all the images
        #  at once. Before reconfiguring the factory, we didn't have to do this
        # for some reason; now we do.
        return list(g.mongo.db.images.find().sort('name'))
    
    @classmethod
    def update_unit(cls, form):
        '''This routine sets the database-stored information for the given
        image to the given values. The document is identified by mongo's
        _id rather than the name because the user may have changed the name.
        The edit date is set to the current date. The tagsField are split based
        on commas.
        '''
        mongoId = ObjectId(form.idField.data)
        image_record = g.mongo.db.images.find_one({'_id': mongoId})
        if image_record is not None:
            image_record['name'] = form.nameField.data
            image_record['filename'] = form.filenameField.data
            image_record['description'] = form.descriptionField.data
            image_record['tags'] = form.tagsField.data.split(',')
            image_record['date'] = get_today()
            g.mongo.db.images.save(image_record)

    @classmethod
    def delete_unit(cls, name):
        '''This routine deletes the image entry with the given nameField.
        It leaves the actual image in place.
        '''
        return g.mongo.db.images.remove({'name': name})

    # Specify the WTForms elements.
    idField = HiddenField('_id')
    nameField = TextField('Name')
    filenameField = TextField('Filename')
    descriptionField = TextField('Description')
    tagsField = TextField('Tag List (separate values using commas, \
                            e.g., tag1, tag2)')

    def initialize(self, name='', action=None, image=None):
        super(Images, self).initialize(action=action)
        # If there is a image, populate the field values.
        if image:
            if action != 'create':
                self.idField.data = str(image.get('_id'))            
            self.nameField.data = image.get('name')
            self.filenameField.data = image.get('filename')
            self.descriptionField.data = image.get('description')
            self.tagsField.data = ', '.join(image.get('tags'))

    def getName(self):
        '''This method returns the name of image, which is
        useful when the CMS user modifies the image name.'''
        return self.nameField.data
