'''
This module defines the features required to support the reading of course
objects in the database. See unit.py for more details.

This particular information unit is read from the CIT database. See a
discussion of the implications of this in programs.py.

Created on Jul 17, 2014

@author: kvlinden
@author: dad32
'''

from datetime import datetime

import requests

from app.units.unit import Unit


class Courses(Unit):
    '''This class encapsulates tools for information units from courses. These
    information units are retrieved from the CIT database and thus this class
    doesn't implement create, update or delete methods; those things must be
    done using CIT tools. It only supports retrieving course lists; individual
    course materials are assumed to be hand-built and available as static
    resources at the standard URL:
        /courses/PROGRAM/COURSE, e.g., /courses/cs/100
    '''
    @classmethod
    def read_units(cls):
        '''This method retrieves course data from CIT's database.'''
        return cls.get_cit_data('CPSC')

    # Utility data and methods...

    # CIT URL for courses (set parameters, e.g., course.dept<-CPSC; course.catalogYear<-2016)...
    # Removed the calendar year option, defaulting to the "current" catalog in all cases. - kvlinden, Jan2017
#    old URL with calendar year option  'https://calvin.edu/api/content/render/false/limit/100/type/json/query/+structureName:course%20+(conhost:cd97e902-9dba-4e51-87f9-1f712806b9c4%20conhost:SYSTEM_HOST)%20+course.dept:*{}*%20+course.catalogYear:{}%20+languageId:1%20%20+deleted:false%20%20+live:true/orderby/course.id'
    coursesUrlTemplate = 'https://calvin.edu/api/content/render/false/limit/100/type/json/query/+structureName:course%20+(conhost:cd97e902-9dba-4e51-87f9-1f712806b9c4%20conhost:SYSTEM_HOST)%20+course.dept:*{}*%20+languageId:1%20%20+deleted:false%20%20+live:true/orderby/course.id'

    @classmethod
    def get_cit_data(cls, department):
        '''Retrieve the course data for the given department from the CIT
        database. Return None if any errors occur.
        '''
        # Create the appropriate URL and read the course data. Convert the data
        # to JSON format. Return None is no course data is found.
        url = cls.coursesUrlTemplate.format(department)
        dataRaw = requests.get(url, verify=False).json()
        if dataRaw is not None:
            data = dataRaw['contentlets']
            if len(data) > 0:
                return data
        return None
