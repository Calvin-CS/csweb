'''
This module defines the features required to support the required CRUD
operations on department objects in the database and to support update/create
forms for those objects. See unit.py and unitForm.py for more details.

Created on Jul 11, 2014

@author: kvlinden
'''

from flask.globals import g
from wtforms.fields.simple import TextField, TextAreaField

from app.units.unit import Unit
from app.units.unitForm import UnitForm
from app.utilities import get_today


class Departments(Unit, UnitForm):
    '''This class encapsulates tools for information units from the department
    collection. There will likely be only one department, CS, so we don't
    implement create or delete, just read and update.
    '''

    @classmethod
    def read_unit(cls, name):
        return g.mongo.db.departments.find_one({'name': name})

    @classmethod
    def update_unit(cls, form):
        '''This routine sets the database-stored information for the given
        department to the given values. The edit date is set to the current
        date.
        '''
        department_record = g.mongo.db.departments.find_one({'name': form.nameField.data})
        if department_record is not None:
            department_record['name'] = form.nameField.data
            department_record['title'] = form.titleField.data
            department_record['tagline'] = form.taglineField.data
            department_record['shortDescription'] = form.shortDescriptionField.data
            department_record['longDescription'] = form.longDescriptionField.data
            department_record['contact'] = form.contactField.data
            department_record['honors'] = form.honorsField.data
            department_record['research'] = form.researchField.data
            department_record['courseSchedule'] = form.courseScheduleField.data
            department_record['date'] = get_today()
            g.mongo.db.departments.save(department_record)

    # Specify the WTForms elements.
    nameField = TextField('Name')
    titleField = TextField('Title')
    taglineField = TextField('Tagline')
    shortDescriptionField = TextAreaField('Short Description (used on the main homepage)')
    longDescriptionField = TextAreaField('Long Description (used on the "About" page)')
    contactField = TextAreaField('Contact information (used on the "Contact us" page)')
    honorsField = TextAreaField('Honors information (used on the "Graduating with Honors" page)')
    researchField = TextAreaField('Research information (used on the "Research" page)')
    courseScheduleField = TextAreaField('Annual course schedule (used on the "Courses" page)')

    def initialize(self, name='', action=None, department=None):
        super(Departments, self).initialize(action=action)
        # If there is a document, populate the field values.
        if department:
            self.nameField.data = department.get('name')
            self.titleField.data = department.get('title')
            self.taglineField.data = department.get('tagline')
            self.shortDescriptionField.data = department.get('shortDescription')
            self.longDescriptionField.data = department.get('longDescription')
            self.contactField.data = department.get('contact')
            self.honorsField.data = department.get('honors')
            self.researchField.data = department.get('research')
            self.courseScheduleField.data = department.get('courseSchedule')
