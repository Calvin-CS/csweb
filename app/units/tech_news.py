'''
Modified news item class for tech news articles. See news.py for more details.

Created on Mar 17, 2015

@author: David Dick dad32
@author: kvlinden
'''
from flask.globals import g
from wtforms.fields.simple import TextField, TextAreaField, HiddenField

from app.units.unit import Unit
from app.units.news import News
from app.units.unitForm import UnitForm
from app.utilities import get_counter, get_today
from utils.findAnalyzeText import *
from random import randrange


class TechNews(Unit, UnitForm):
    '''This class encapsulates tools for information units from the tech articles
    It is similar to the news unit, but calls other functions.
    '''

    # Number of tech-news items to display on the homepage.
    TECH_NEWS_LIMIT = 2
    # RSS feeds providing tech-news articles
    TECH_NEWS_FEEDS = \
        ['http://www.calvin.edu/rss/news-and-stories.html',
         'http://feeds2.feedburner.com/ziffdavis/pcmag/breakingnews',
         'http://feeds2.feedburner.com/ziffdavis/pcmag/commentary',
         'http://rssnewsapps.ziffdavis.com/forwardthinking.xml',
         'http://www.technologyreview.com/computing/rss/',
         'http://rss.acm.org/technews/TechNews.xml',
         'http://phys.org/rss-feed/technology-news/',
         'http://feeds.bbci.co.uk/news/technology/rss.xml',
         'http://feeds.arstechnica.com/arstechnica/index?format=xml'
         ]
    # Mongo name values for the positive and negative tech news words.
    TECH_NEWS_BAD_WORDS_NAME = 'tech_news_bad'
    TECH_NEWS_GOOD_WORDS_NAME = 'tech_news_good'


    @classmethod
    def update_unit(cls, newsList, unitsDisplay):
        '''This method updates the information specified in the given
        information unit. The edit date is set to the current date.
        The administrator cannot change the article name, so it's not
        on the form and must, therefore, be passed separately.
        The id for this is limited to currently 3 articles.
        '''
        if len(newsList) > 0:
            if len(newsList) < unitsDisplay:
                unitsDisplay = len(newsList)

            articlesDisplay = []
            while len(articlesDisplay) < unitsDisplay:
                if len(articlesDisplay) == 0:
                    int1 = randrange(0, min(len(newsList), 3))
                    articlesDisplay = articlesDisplay + [int1]
                elif len(articlesDisplay) == 1:
                    # articlesDisplay.append(int1)
                    int2 = randrange(0, min(len(newsList), 3))
                    articlesDisplay = articlesDisplay + [int2]
                    if articlesDisplay[0] == articlesDisplay[1]:
                        articlesDisplay[1] = articlesDisplay[0] + 1
                else:
                    intTemp = randrange(0, min(len(newsList), unitsDisplay+7))
                    while (intTemp in articlesDisplay):
                        intTemp = randrange(0, min(len(newsList), unitsDisplay+7))
                    articlesDisplay = articlesDisplay + [intTemp]
                    
            j = 0
            for i in articlesDisplay:
                article_record = g.mongo.db.news.find_one({'name':
                                                           'tech_news_'+str(j)})
                if article_record is not None:
                    article_record['title'] = newsList[i].get('title')
                    article_record['summary'] = newsList[i].get('links')[0].get('href')
                    article_record['content'] = newsList[i].get('summary')
                    article_record['date'] = get_today()
                    g.mongo.db.news.save(article_record)
                else:
                    article_record = {}
                    article_record['name'] = 'tech_news_'+str(j)
                    article_record['title'] = newsList[i].get('title')
                    article_record['summary'] = newsList[i].get('links')[0].get('href')
                    article_record['content'] = newsList[i].get('summary')
                    article_record['date'] = get_today()
                    g.mongo.db.news.insert(article_record)  # @UndefinedVariable
                j = j+1
        else:
            print 'Error, unable to find news'
            print len(newsList)

    @classmethod
    def read_unit(cls, name):
        return g.mongo.db.news.find_one({'name': name})

    @classmethod
    def read_units(cls, refreshList = True, unitsDisplay=3):
        '''if refreshList is True:
            refresh the tech news feed in the database (ie. the home page)
        else:
            display the news articles without refreshing home page content'''
        badText = g.mongo.db.wordBank.find_one({'name': cls.TECH_NEWS_BAD_WORDS_NAME}).get('data')
        goodText = g.mongo.db.wordBank.find_one({'name': cls.TECH_NEWS_GOOD_WORDS_NAME}).get('data')
        newsList = display_my_results(goodText, badText, cls.TECH_NEWS_FEEDS)
        if refreshList:
            cls.update_unit(newsList, unitsDisplay)
        return newsList

    @classmethod
    def up_unit(cls, url, inNews=False):
        '''This method updates the information specified in the given
        information unit. The edit date is set to the current date.
        The administrator cannot change the article name, so it's not
        on the form and must, therefore, be passed separately.
        '''

        if inNews:
            newsArray = g.mongo.db.news.find().sort('date', -1)
            for article in newsArray:
                if article.get('summary').replace('/', '').replace('?', '') == url:
                    upArticle(article.get('content') + ' ' + article.get('title'), cls.TECH_NEWS_GOOD_WORDS_NAME)
                    break
        else:
            newsArray = cls.read_units(refreshList=False)
            for article in newsArray:
                if article.get('links')[0].get('href').replace('/', '').replace('?', '') == url:
                    upArticle(article.get('summary') + ' ' + article.get('title'), cls.TECH_NEWS_GOOD_WORDS_NAME)
                    break

    @classmethod
    def down_unit(cls, url, inNews=False):
        '''This method updates the information specified in the given
        information unit. The edit date is set to the current date.
        The administrator cannot change the article name, so it's not
        on the form and must, therefore, be passed separately.
        '''
        if inNews:
            newsArray = g.mongo.db.news.find().sort('date', -1)
            for article in newsArray:
                if article.get('summary').replace('/', '').replace('?', '').replace('?','') == url:
                    downArticle(article.get('content') + ' ' + article.get('title'), cls.TECH_NEWS_BAD_WORDS_NAME)
                    break

        else:
            newsArray = cls.read_units(refreshList=False)
            for article in newsArray:
                if article.get('links')[0].get('href').replace('/', '').replace('?', '') == url:
                    downArticle(article.get('summary') + ' ' + article.get('title'), cls.TECH_NEWS_BAD_WORDS_NAME)
                    break

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
