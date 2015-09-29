'''
This module defines the root class for working with information units from
the database.

Its subclasses are assumed to have the same name as is used in the database.
They should work only with the domain representations of the information units
from the database; the views methods transform domain information to rhetorical
content.

Created on Jul 8, 2014

@author: kvlinden
'''


class Unit():
    '''All information units must implement these class methods. They operate
    entirely on domain content from the database. There is no support for
    transactions; these routines will walk on edits/deletions being made by
    others.
    '''
    # No instance data is stored; doing so would be pointless given that it
    # couldn't be stored from one (stateless) HTTP request to the next.

    # We use class methods because sometimes it's useful to implement utility
    # data items and methods to be called when overriding these methods. That
    # requires access to class data/methods, which isn't possible with static
    # methods. Other than this, class/static methods behave similarly.

    @classmethod
    def create_unit(cls, form):
        '''This method should create a new database document based on the
        information in the given form and return the name of that document.
        '''
        raise NotImplementedError

    @classmethod
    def read_unit(cls, name):
        '''This method should return the dict representation of the information
        unit for the given unit name from the database.
        '''
        raise NotImplementedError

    @classmethod
    def read_units(cls, limit=None):
        '''This method should return a list of the dict representations
        information units for the given collection. If limit is none, return
        all instances; if limit > 0, return a list of limit results;
        if limit <= 0, return None.
        '''
        raise NotImplementedError

    @classmethod
    def update_unit(cls, form):
        '''This method should update the database using the information from
        the specified form.
        '''
        raise NotImplementedError

    @classmethod
    def delete_unit(cls, unitName):
        '''This method should delete the information unit for the given unit
        name from the database.
        '''
        raise NotImplementedError

    @staticmethod
    def merge_records(cit_record, cs_record):
        '''This (static) method merges individual records from the CIT and CS
        databases, returning only one record if the other is missing and
        overwriting CIT entries with CS entries from entries with the same
        name.
        '''
        if cit_record is None:
            return cs_record
        if cs_record is None:
            return cit_record
        result = cit_record
        for key in cs_record:
            result[key] = cs_record[key]
        return result

    @staticmethod
    def merge_lists(cit_list, cs_list):
        '''This (static) method creates a union of the given CIT and CS lists,
        merging any records with the same name.
        '''
        if cit_list is None or len(cit_list) < 1:
            return cs_list
        if cs_list is None or len(cs_list) < 1:
            return cit_list
        result = cs_list
        for cit_record in cit_list:
            cs_cit_index = Unit.find_record_in_list(cit_record, result)
            if cs_cit_index >= 0:
                result[cs_cit_index] = Unit.merge_records(cit_record,
                                                          result[cs_cit_index])
            else:
                result.append(cit_record)
        return result

    @staticmethod
    def find_record_in_list(target, source_list):
        '''The method returns the index of the element of the source list that
        has the same name as the target record.
        '''
        i = 0
        for record in source_list:
            if 'name' in record and \
               'name' in target and \
               record['name'] == target['name']:
                return i
            i += 1
        return None
