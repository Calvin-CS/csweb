'''
This module contains database construction utilities for use in testing,
development and production. The calling program provides the appropriate
context and data. The number of collections must match in length and order
with the structure of the data structures in data/dev.py and data/test.py.

Created on Jan 23, 2014

@author: kvlinden
'''

empty_db = [[], [], [], [], [], [], [], [], []]


def db_reset(mongo, data=empty_db):
    '''This routine clears and then rebuilds the csweb database. '''
    collections = [mongo.db.programs,
                   mongo.db.documents,
                   mongo.db.resources,
                   mongo.db.departments,
                   mongo.db.users,
                   mongo.db.images,
                   mongo.db.scholarships,
                   mongo.db.news,
                   mongo.db.counters,
                   mongo.db.wordBank]
    db_clear(collections)
    for i in range(len(collections)):
        collections[i].insert(data[i])


def db_clear(collections):
    '''This routine removes all the collections in the given list of
    mongodb collections completely.
    '''
    for collection in collections:
        collection.drop()
