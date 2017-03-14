'''
This module defines the features required to support the reading of
faculty/staff objects in the database. See unit.py for more details.

This particular information unit is read from the CIT database. See a
discussion of the implications of this in programs.py.

This unit has not been refactored to use the Unit merge features.

Created on Jul 17, 2014

@author: kvlinden
@author: dad32
'''

import requests

from app.units.unit import Unit


class People(Unit):
    '''This class encapsulates tools for information units from people. These
    information units are retrieved from the CIT database and thus this class
    doesn't implement create, update or delete methods; those things must be
    done using CIT tools. It only supports retrieving people lists; content for
    individual people is assumed to be hand-built and available as static
    resources at the standard, college-wide URL:
        http://www.calvin.edu/~LOGIN_ID.
    '''

    # CIT URL for people (set parameters, marked by {} in the template, for department or userid)...
    peopleImageTemplate = 'http://calvin.edu/contentAsset/image/{}/filter/Resize/resize_w/142'
    departmentUrlTemplate = 'https://calvin.edu/api/content/render/false/limit/50/type/json/query/+structureName:CcProfiles%20+%28conhost:cd97e902-9dba-4e51-87f9-1f712806b9c4%20conhost:SYSTEM_HOST%29%20+CcProfiles.academicDepartment:{}%20+languageId:1%20%20+deleted:false%20%20+live:true%20+live:true/orderby/CcProfiles.lastname'
    personUrlTemplate = 'https://calvin.edu/api/content/render/false/limit/50/type/json/query/+structureName:CcProfiles%20+%28conhost:cd97e902-9dba-4e51-87f9-1f712806b9c4%20conhost:SYSTEM_HOST%29%20+CcProfiles.id:{}%20+languageId:1%20%20+deleted:false%20%20+live:true%20+live:true'

    # People to add to the department manually by Calvin loginID.
    contributing_faculty_ids = ['rpruim', 'stob', 'bp28', 'avedra', 'dsc8']

    @classmethod
    def read_units(cls):
        '''This method retrieves person data from CIT's DB for all CS-related faculty, emeriti, adjuncts, staff.'''
        cs_people = cls.get_department_data('CPSC')
        people_by_role = cls.split_cspeople_by_role(cs_people)
        contributing_people = cls.get_people_data(cls.contributing_faculty_ids)
        if contributing_people is not None:
            people_by_role['contributing'] = contributing_people
        cls.update_person_image_and_email_values(people_by_role)
        return people_by_role

    @classmethod
    def get_department_data(cls, department):
        '''Retrieve the faculty data for the given department from the CIT DB. Return None if any errors occur.'''
        # Create the appropriate URL to get JSON people data for the given department, all in one call to the API.
        url = cls.departmentUrlTemplate.format(department)
        dataRaw = requests.get(url, verify=False).json()
        if dataRaw is not None:
            data = dataRaw['contentlets']
            if len(data) > 0:
                return data
        return None

    @classmethod
    def split_cspeople_by_role(cls, cs_people):
        '''Return a dictionary with the roles as the key and lists of people records as the values.'''
        faculty = []
        emeriti = []
        staff = []
        exfaculty = ['smn4', 'jnyhoff'] # CIT keeps these people on the system for some reason.
        for person in cs_people:
            if 'Academic' in person.get('jobFunction', ''):
                if not (person.get('id') in exfaculty):
                    faculty.append(person)
            elif 'Emeritus' in person.get('jobFunction', ''):
                if not (person.get('id') in exfaculty):
                    emeriti.append(person)
            else:
                staff.append(person)
        return {'faculty': faculty, 'emeriti': emeriti, 'staff': staff}

    @classmethod
    def get_people_data(cls, person_ids):
        '''Retrieve the faculty data for the given user IDS. Return None if any errors occur.'''
        # Create the appropriate URL and read the people data for the given
        # department. Convert the data to JSON format. Return None is no
        # people data is found.
        result = []
        for id in person_ids:
            url = cls.personUrlTemplate.format(id)
            dataRaw = requests.get(url, verify=False).json()
            if dataRaw is not None:
                data = dataRaw['contentlets']
                if len(data) > 0:
                    result.append(data[0])
        result.sort(cmp=None, key=lambda person: person.get('lastName'), reverse=False)
        return result

    @classmethod
    def update_person_image_and_email_values(cls, people_by_role):
        '''Modifies the given dictionary by changing image URLs and email IDs as needed.'''
        for role, people in people_by_role.iteritems():
            for person in people:
                # Clean up some of CIT's data fields.
                if 'binaryimageContentAsset' in person:
                    person['image'] = cls.peopleImageTemplate.format(
                        person['binaryimageContentAsset'])
                if 'emailAddress' in person:
                    person['email'] = person['emailAddress'].split('@')[0]
