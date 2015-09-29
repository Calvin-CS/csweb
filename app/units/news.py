'''
This module defines the features required to support the required CRUD
operations on news article objects in the database and to support update/create
forms for those objects. See unit.py and unitForm.py for more details.

Created on Jul 11, 2014

@author: kvlinden
'''
from flask.globals import g
from wtforms.fields.simple import TextField, TextAreaField, HiddenField

from app.units.unit import Unit
from app.units.unitForm import UnitForm
from app.utilities import get_counter, get_today


class News(Unit, UnitForm):
    '''This class encapsulates tools for information units from the news
    articles collection. We will consider getting this information from
    the CIT news database.'''

    @classmethod
    def create_unit(cls, form):
        '''This method should create a new database article based on the
        information in the given form and return the name of that article.
        The name is automatically set to 'news_' plus a unique counter and
        the edit date is set to the current date.'''
        record = {}
        record['name'] = 'news_' + str(get_counter('news'))
        record['title'] = form.titleField.data
        record['summary'] = form.summaryField.data
        record['content'] = form.contentField.data
        record['date'] = get_today()
        g.mongo.db.news.insert(record)  # @UndefinedVariable
        return record['name']

    @classmethod
    def read_unit(cls, name):
        return g.mongo.db.news.find_one({'name': name})

    @classmethod
    def read_units(cls, limit=None):
        if limit is None:
            return g.mongo.db.news.find().sort('date', -1)
        else:
            return g.mongo.db.news.find().sort('date', -1).limit(limit)

    @classmethod
    def update_unit(cls, form):
        '''This method updates the information specified in the given
        information unit. The edit date is set to the current date.
        The administrator cannot change the article name, so it's not
        on the form and must, therefore, be passed separately.
        '''
        article_record = g.mongo.db.news.find_one({'name':
                                                   form.nameField.data})
        if article_record is not None:
            article_record['title'] = form.titleField.data
            article_record['summary'] = form.summaryField.data
            article_record['content'] = form.contentField.data
            article_record['date'] = get_today()
            g.mongo.db.news.save(article_record)

    @classmethod
    def delete_unit(cls, name):
        return g.mongo.db.news.remove({'name' : name})

    # Specify the WTForms elements.
    nameField = HiddenField('Name')
    titleField = TextField('Title')
    summaryField = TextField('Summary')
    contentField = TextAreaField('Content')

    def initialize(self, action=None, unit=None):
        super(News, self).initialize(action=action)
        if unit:
            self.nameField.data = unit.get('name')
            self.titleField.data = unit.get('title')
            self.summaryField.data = unit.get('summary')
            self.contentField.data = unit.get('content')
