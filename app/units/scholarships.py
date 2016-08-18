'''
This module defines the features required to support the reading of
scholarship objects in the database. See unit.py for more details.

This particular information unit is read from the CIT and CS databases
(see a discussion of the implications of this in programs.py), so this
class combines elements of both databases based on the scholarship title,
which must be specified correctly in the given name_map.

Created on Jul 17, 2014

@author: dad32
@author: kvlinden
'''

from flask.globals import g
import requests
from wtforms.fields.simple import TextField, TextAreaField

from app.units.unit import Unit
from app.units.unitForm import UnitForm
from app.utilities import get_today


class Scholarships(Unit, UnitForm):
    '''This class encapsulates tools for information units from scholarships.
    These information units are partially retrieved from the CIT database, but
    the CS database can contribute entries as well. Thus, this class does
    implement all the CRUD methods.
    '''

    @classmethod
    def create_unit(cls, form):
        '''This routine creates an scholarship based on the given values.
        The edit date is set to the current date. The unique name is set by
        the user, not by the system. This only creates the CS db entry,
        not a CIT database entry.'''
        record = {}
        record['name'] = form.nameField.data
        record['title'] = form.titleField.data
        record['ordinal'] = form.ordinalField.data
        record['shortDescription'] = form.shortDescriptionField.data
        record['longDescription'] = form.longDescriptionField.data
        record['applyInformation'] = form.applicationInfoField.data
        record['programs'] = form.programsField.data.split(', ')
        record['url'] = form.urlField.data
        record['recipients'] = form.recipientsField.data
        record['date'] = get_today()
        return g.mongo.db.scholarships.insert(record)

    # Mapping from CIT scholarship titles to CS scholarship names...
    # This key must match the key name in the CIT database. They have a
    # titlealpha as well, but it appears to swap first and last names.
    CIT_TITLE_KEY = 'title'
    # These titles and names must match those found in the CIT and CS
    # databases respectively. The short name must be a unique sub-set
    # of the full title so that the reverse search in read_unit() works
    # properly.
    cit2cs_name_map = {}
    cit2cs_name_map[u'DornerWorks Computer&Software Engineering Scholarship'] = u'dornerworks'
    cit2cs_name_map[u'Gordon J. VanderBrug Scholarship'] = u'vanderbrug'
    cit2cs_name_map[u'Steven DeRose Family Scholarship'] = u'derose'
    cit2cs_name_map[u'Larry and Sharlene Nyhoff Scholarship in Computer Science'] = u'nyhoff'
    cit2cs_name_map[u'NSF Scientific Computing Scholarship'] = u'isri'
    cit2cs_name_map[u'Patricia S. Duthler Computer Science Scholarship'] = u'duthler'
    cit2cs_name_map[u'Grateful Computer Science Alumnus Scholarship'] = u'grateful'
    cit2cs_name_map[u'George and Gayle Hommes Family Scholarship'] = u'hommes'
    cit2cs_name_map[u'Michigan Industrial Tools Scholarship'] = u'tools'
    cit2cs_name_map[u'Strategic Partners - Spectrum Health Scholarship'] = u'spectrum'
    cit2cs_name_map[u'Strategic Partners - Open Systems Technology Scholarship'] = u'open'

    @classmethod
    def read_units(cls):
        '''This method retrieves scholarship data from the CIT and CS databases
        and returns the union of the two lists, merging entries that share the
        same name. CS database entries are assumed to have name fields.
        '''
        cit_list = cls.get_cit_scholarships('CPSC')
        # Add a name entry to each CIT record based on the title-name mapping.
        for cit_entry in cit_list:
            if cit_entry[cls.CIT_TITLE_KEY] in cls.cit2cs_name_map:
                cit_entry['name'] = \
                    cls.cit2cs_name_map[cit_entry[cls.CIT_TITLE_KEY]]
        return Unit.merge_lists(cit_list,
                                list(g.mongo.db.scholarships.find().sort('ordinal')))

    @classmethod
    def read_unit(cls, name):
        '''This routine find an document with the given nameField.'''
        return Unit.merge_records(
            cls.get_cit_scholarship('CPSC', name),
            g.mongo.db.scholarships.find_one({'name': name})
            )

    @classmethod
    def update_unit(cls, form):
        '''This routine sets the database-stored information for the given
        document to the given values. The document is identified by mongo's
        _id rather than the name because the user may have changed the name.
        The edit date is set to the current date.
        '''
        name = form.nameField.data
        scholarship_record = g.mongo.db.scholarships.find_one({'name': name})
        if scholarship_record is not None:
            scholarship_record['name'] = form.nameField.data
            scholarship_record['title'] = form.titleField.data
            scholarship_record['ordinal'] = int(form.ordinalField.data)
            scholarship_record['shortDescription'] = form.shortDescriptionField.data
            scholarship_record['longDescription'] = form.longDescriptionField.data
            scholarship_record['applicationInfo'] = form.applicationInfoField.data
            scholarship_record['programs'] = form.programsField.data.split(', ')
            scholarship_record['url'] = form.urlField.data
            scholarship_record['recipients'] = form.recipientsField.data
            scholarship_record['date'] = get_today()
            g.mongo.db.scholarships.save(scholarship_record)

    @classmethod
    def delete_unit(cls, name):
        '''This routine deletes the scholarship entry with the given nameField.
        '''
        return g.mongo.db.scholarships.remove({'name': name})

    # The WTForms elements
    nameField = TextField('Name (Set this on creation; don&rsquo;t change it)')
    titleField = TextField('Title (Replaces CIT&rsquo;s title)')
    ordinalField = TextField('Ordinal (sets the display order manually, be consistent with other scholarships)')
    shortDescriptionField = TextAreaField('Short Description (used in lists)')
    longDescriptionField = TextAreaField('Long Description (added to \
                                CIT&rsquo;s description)')
    applicationInfoField = TextAreaField('Application Procedure')
    programsField = TextField('Applicable Programs (separate values using \
                                commas, e.g., bcs, cs, is, dc, ds)')
    urlField = TextField('External URL (if any)')
    recipientsField = TextAreaField('Recipients')

    def initialize(self, name='', action=None, scholarship=None):
        super(Scholarships, self).initialize(action=action)
        # If there is a scholarship, populate the field values.
        if scholarship:
            self.nameField.data = scholarship.get('name')
            self.titleField.data = scholarship.get('title')
            self.ordinalField.data = scholarship.get('ordinal')
            self.shortDescriptionField.data = scholarship.get('shortDescription')
            self.longDescriptionField.data = scholarship.get('longDescription')
            self.applicationInfoField.data = scholarship.get('appInfo')
            self.programsField.data = ', '.join(scholarship.get('programs'))
            self.urlField.data = scholarship.get('url')
            self.recipientsField.data = scholarship.get('recipients')

    def getName(self):
        '''This method returns the name of document, which is
        useful when the CMS user modifies the document name.'''
        return self.nameField.data

    # Utility data and methods...
    # Mapping from our program IDs to CIT's names is done by merging
    # our data entries (with name) with theirs (with title).

    scholarshipsUrlTemplate = 'https://upbeat.calvin.edu/api/content/render/false/type/json/query/+structureName:CcScholarships%20+%28conhost:cd97e902-9dba-4e51-87f9-1f712806b9c4%20conhost:SYSTEM_HOST%29%20+CcScholarships.department:*{}*%20+languageId:1%20%20+deleted:false%20%20+live:true/orderby/CcScholarships.title'
    scholarshipUrlTemplate =  'https://upbeat.calvin.edu/api/content/render/false/type/json/query/+structureName:CcScholarships%20+%28conhost:cd97e902-9dba-4e51-87f9-1f712806b9c4%20conhost:SYSTEM_HOST%29%20+CcScholarships.department:*{}*%20+CcScholarships.title:*{}*%20+languageId:1%20%20+deleted:false%20%20+live:true/orderby/CcScholarships.title'

    @classmethod
    def get_cit_scholarships(cls, department):
        '''Retrieve the scholarship data for the given department from the CIT
        database. Return None if any errors occur.
        '''
        # Create the appropriate URL and read the people data for the given
        # department. Convert the data to JSON format. Return None is no
        # people data is found.
        url = cls.scholarshipsUrlTemplate.format(department)
        dataRaw = requests.get(url, verify=False).json()
        if dataRaw is not None:
            data = dataRaw['contentlets']
            if len(data) > 0:
                for scholarship in data:
                    if '/' in scholarship['title']:
                        scholarship['title'] = scholarship['title'].replace('/', '&', 60)
                return data
        return None

    @classmethod
    def get_cit_scholarship(cls, department, scholarship):
        '''Retrieve an individual scholarship entry for the given department
        from the CIT database. Return None if any errors occur.
        '''
        url = cls.scholarshipUrlTemplate.format(department, scholarship)
        dataRaw = requests.get(url, verify=False).json()
        if dataRaw is not None:
            data = dataRaw['contentlets']
            print data
            if len(data) > 0:
                return data[0]
        else:
            url = cls.scholarshipUrlTemplate.format(department, scholarship.replace('&','/'))
            dataRaw = requests.get(url, verify=False).json()
            if dataRaw is not None:
                data = dataRaw['contentlets']
                if len(data) > 0:
                    if '/' in data[0]['title']:
                        data['title'][0] = data[0]['title'].replace('/', ' ', 60)
                    return data[0]
        return None
