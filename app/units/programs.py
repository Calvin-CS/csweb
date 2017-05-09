'''
This module defines the features required to support the reading of program
objects in the database. See unit.py for more details.

Because a program's model schedule is stored locally, while the rest of the
data comes from CIT, this class supports updating the model schedule only.

This particular information unit is (mostly) read from the CIT database, which
means that it does not support create or delete operations. This is
generally good in that we reuse institutional data, but has some undesirable
consequences:
- The department must go though CIT to get content edited.
- The system must use CIT's fields & field names, which are more
  webpage-oriented than information-oriented.
- CIT doesn't recognize the DA major and doesn't store the minor for
  secondary education.
CIT should provide a hierarchical, JSON-based program representation rather
than a string-based representation.

Created on Jul 14, 2014

@author: kvlinden
@author: dad32
'''

import re

from flask.globals import g
import requests
from wtforms.fields.simple import TextAreaField, HiddenField

from app.units.scholarships import Scholarships
from app.units.unit import Unit
from app.units.unitForm import UnitForm
from app.utilities import get_today, create_hyperlink


class Programs(Unit, UnitForm):
    '''This class encapsulates tools for information units from programs.
    These information units are retrieved from the CIT database and thus this
    class doesn't implement create, update or delete methods; those things
    must be done using CIT tools.'''

    @classmethod
    def read_unit(cls, name, scholarships=None):
        '''This method retrieves merges program data from the CIT
        and CS databases.
        '''
        result = Unit.merge_records(
            cls.get_cit_data(name),
            g.mongo.db.programs.find_one({'name': name})
        )
        if result:
            # Modify the course hyperlinks to link to our own pages.
            if 'courses' in result:
                result['courses'] = \
                    cls.fix_courses(result['courses'])
            if 'minorCourses' in result:
                result['minorCourses'] = \
                    cls.fix_courses(result['minorCourses'])
            # Add scholarships regardless of where the program comes from.
            # Use the scholarships parameter if given, otherwise read them.
            if scholarships is None:
                scholarships = Scholarships.read_units()
            result['scholarships'] = \
                cls.get_scholarships(name, scholarships)
        return result

    @classmethod
    def read_units(cls):
        '''This method retrieves program data from CIT for all department
        programs and combines it in one list. It calls read_unit(), which
        actually reads more information than is required for the current
        list of academic programs (e.g., course lists and scholarships), but
        this allows us to add information to the list if we choose to do so
        later. The secondary education program is not currently stored at CIT.
        '''
        result = []
        # Read a master scholarships list to be used multiple times.
        scholarships = Scholarships.read_units()
        for programName in ['bcs', 'cs', 'is', 'ds', 'dc', 'csm', 'ism', 'dsm', 'dam']:
            program = cls.read_unit(programName, scholarships=scholarships)
            if program is not None:
                result.append(program)
        return result

    @classmethod
    def update_unit(cls, form):
        '''This routine sets the database-stored information for the given
        program to the given values. Because the administrator cannot edit
        the name field, we don't show it but key off of it for the query.
        The edit date is set to the current date.
        '''
        name = form.nameField.data
        program_record = g.mongo.db.programs.find_one({'name': name})
        if program_record is not None:
            program_record['modelSchedule'] = form.modelScheduleField.data
            program_record['date'] = get_today()
            g.mongo.db.programs.save(program_record)

    nameField = HiddenField('name')
    modelScheduleField = TextAreaField('Model Schedule (CIT holds all the other data)')

    def initialize(self, name=None, action=None, document=None):
        super(Programs, self).initialize(action=action)
        # If there is a document, populate the field values.
        if document:
            self.nameField.data = name
            self.modelScheduleField.data = document.get('modelSchedule')

    # Utility data and methods...
    # Mapping from our program IDs to CIT's names...
    cs2cit_program_name_mapping = {}
    cs2cit_program_name_mapping['bcs'] = 'CPSC.BCS.MAJ' #'BCS.CPSC'
    cs2cit_program_name_mapping['cs'] = 'CPSC.MAJ'
    cs2cit_program_name_mapping['csm'] = 'CPSC.MIN'
    cs2cit_program_name_mapping['is'] = 'INSYS.MAJ'
    cs2cit_program_name_mapping['ism'] = 'INSYS.MIN'
    cs2cit_program_name_mapping['ds'] = 'DATA.MAJ'
    cs2cit_program_name_mapping['dsm'] = 'DATA.MIN'
    cs2cit_program_name_mapping['dam'] = 'ANLYT.MIN'
    cs2cit_program_name_mapping['dc'] = 'CASCS.MAJ'
    #cs2cit_program_name_mapping['dcm'] = 'CASCS.MIN'
    #cs2cit_program_name_mapping['bada'] = 'digital-art'

    # CIT URL for program resources (set program name parameter) ...
#    programUrlTemplate = 'https://calvin.edu/api/content/render/false/type/json/query/+structureName:CcAcademicProgram%20+%28conhost:cd97e902-9dba-4e51-87f9-1f712806b9c4%20conhost:SYSTEM_HOST%29%20+CcAcademicProgram.academicDepartment:*C*S*%20+languageId:1%20%20+deleted:false%20%20+CcAcademicProgram.academicProgramCode:{}%20+live:true/orderby/undefined%20desc'
    programUrlTemplate = 'https://calvin.edu/api/content/render/false/query/+contentType:CcMajorsAndPrograms%20+CcMajorsAndPrograms.programCode:*{}*%20+deleted:false%20+live:true/orderby/modDate%20d'

    @classmethod
    def get_cit_data(cls, name):
        '''Retrieve the program data for the given name from the CIT
        database. Return None if any errors occur.
        '''
        # Compute the URL for CIT's program API for the given programId.
        if name in cls.cs2cit_program_name_mapping:
            mappedName = cls.cs2cit_program_name_mapping[name]
        else:
            return None
        url = cls.programUrlTemplate.format(mappedName)

        if url is None:
            return None
        # Get the data from the API and convert it to JSON.
        dataRaw = requests.get(url, verify=True).json()

        if dataRaw is None or \
                not ('contentlets' in dataRaw) or \
                        len(dataRaw['contentlets']) < 1:
            return None

        # Return the actual data from the raw result.
        return dataRaw['contentlets'][0]

    # String replacements that hack CIT's text for our site. Yuck!
    CIT_HREF = 'class="courseLink" href="#" data-reveal-id="COURSE"id="'
    programStringReplacements = \
        ('<h1>', '<h2>'), \
        ('</h1>', '</h2>'), \
        (CIT_HREF + 'CS-', 'href="/courses/cs/'), \
        (CIT_HREF + 'IS-', 'href="/courses/is/'), \
        (CIT_HREF + 'DATA-', 'href="/courses/ds/')
        # ('class="courseLink" href="#" data-reveal-id="COURSE"id="ENGR-',
        #  'href="http://www.calvin.edu/academics/majors-minors/course-description.html?course=ENGR-'), \
        # ('class="courseLink" href="#" data-reveal-id="COURSE"id="MATH-',
        #  'href="http://www.calvin.edu/academics/majors-minors/course-description.html?course=MATH-'), \
        # ('class="courseLink" href="#" data-reveal-id="COURSE"id="STAT-',
        #  'href="http://www.calvin.edu/academics/majors-minors/course-description.html?course=STAT-'), \
        # ('class="courseLink" href="#" data-reveal-id="COURSE"id="BUS-',
        #  'href="http://www.calvin.edu/academics/majors-minors/course-description.html?course=BUS-'), \
        # ('class="courseLink" href="#" data-reveal-id="COURSE"id="ECON-',
        #  'href="http://www.calvin.edu/academics/majors-minors/course-description.html?course=ECON-'), \
        # ('class="courseLink" href="#" data-reveal-id="COURSE"id="ENGL-',
        #  'href="http://www.calvin.edu/academics/majors-minors/course-description.html?course=ENGL-'), \
        # ('class="courseLink" href="#" data-reveal-id="COURSE"id="ARTS-',
        #  'href="http://www.calvin.edu/academics/majors-minors/course-description.html?course=ARTS-'), \
        # ('class="courseLink" href="#" data-reveal-id="COURSE"id="CAS-',
        #  'href="http://www.calvin.edu/academics/majors-minors/course-description.html?course=CAS-'), \
        # ('class="courseLink" href="#" data-reveal-id="COURSE"id="ASTR-',
        #  'href="http://www.calvin.edu/academics/majors-minors/course-description.html?course=ASTR-'), \
        # ('class="courseLink" href="#" data-reveal-id="COURSE"id="BIOL-',
        #  'href="http://www.calvin.edu/academics/majors-minors/course-description.html?course=BIOL-'), \
        # ('class="courseLink" href="#" data-reveal-id="COURSE"id="CHEM-',
        #  'href="http://www.calvin.edu/academics/majors-minors/course-description.html?course=CHEM-'), \
        # ('class="courseLink" href="#" data-reveal-id="COURSE"id="PHYS-',
        #  'href="http://www.calvin.edu/academics/majors-minors/course-description.html?course=PHYS-')

    @staticmethod
    def multiple_replacer(*key_values):
        '''This method compiles the given string replacements and returns a
        replacement function. It is designed to go through the string once
        rather than once per replacement. It is based on code found here:
        http://stackoverflow.com/questions/6116978/python-replace-multiple-strings
        '''
        replace_dict = dict(key_values)
        replacement_function = lambda match: replace_dict[match.group(0)]
        pattern = re.compile("|".join([re.escape(k) for k, v in key_values]), re.M)
        return lambda string: pattern.sub(replacement_function, string)

    @classmethod
    def multiple_replace(cls, string, *key_values):
        '''This method does the actual replacements. More more information,
        see multiple_replacer().
        '''
        return cls.multiple_replacer(*key_values)(string)

    @classmethod
    def fix_courses(cls, courses):
        '''This method modifies a list of courses to included course
        links to our our own pages rather than to the CIT pages included
        in the CIT database.
        '''
        return cls.multiple_replace(courses,
                                    *cls.programStringReplacements)

    @classmethod
    def get_scholarships(cls, programName, scholarships):
        '''This method creates a list of scholarships applicable to the given
        program. It could use utilities/create_scholarships_list(), but that
        method must create formatted text, not lists, and it filters entries
        based on the given program name.
        The method receives a list of scholarships so that it doesn't have to
        keep re-reading the same list for each program in a long program list.
        '''
        formatedText = '''<p>Students in this program are eligible for the
        following scholarships and awards:</p><ul>'''
        # Only read the scholarship units if we haven't already done so.
        for scholarship in scholarships:
            if scholarship.get('programs') is None or \
                            programName not in scholarship.get('programs'):
                continue
            formatedText += '<li>'
            if scholarship.get('url'):
                url = scholarship.get('url')
            else:
                url = '/scholarships/' + scholarship.get('name')
            formatedText += '<strong>' + \
                            create_hyperlink(url, scholarship.get('title')) + \
                            '</strong>'
            formatedText += ' &ndash; '
            if scholarship.get('shortDescription') is not None:
                formatedText += scholarship.get('shortDescription')
            formatedText += '</li>'
        formatedText += '</ul>'
        return formatedText
