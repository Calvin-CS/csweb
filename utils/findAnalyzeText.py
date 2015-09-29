'''
This mechanism reads RSS feeds from web sites, parses through the data.
The mechanism then sends the news to analyzeText.py file and returns the list 
of analyzed text.
Created October 1, 2014

@author: David Dick dad32
'''
from __future__ import division
from functools import wraps
from decimal import *
import json
from pprint import pprint
import feedparser
import urllib2
from xml.dom import minidom, Node
import time
from datetime import datetime, timedelta, date
import numpy as np
from sklearn.naive_bayes import GaussianNB
from utils.analyzeText import analyzeText
import string
from flask.globals import g


def parseText(messages):
    '''
    Parse through an arrays of sentences and \n characters to get the words.
    '''
    returnWords = []

    for message in messages.split('\n'):
        for wordGiven in message.split(' '):
            for word in parseWords(wordGiven):
                returnWords.append(word)
    return returnWords


def parseWords(string):
    ''' Parse through the letters of a string
and clean out 'bad' letters that python isn't going to like.... non ascii.
Also ignore html tags and splits on the \n character.
'''
    wordReturn = []
    currentWord = ""
    ignore = False
    for letter in string:
        if ignore and letter == '>':
            ignore = False
            continue
        if ignore:
            continue
        if letter in ('<', '>'):
            ignore = True
            continue
        if letter in (' ', u'\x97', u'\x92', u'\x92s', '\n'):
            # Hex characters aren't implicitly converted to unicode.
            wordReturn.append(currentWord)
            currentWord = ""
        elif letter in ('.', '?', '!', '\\'):
            continue
        else:
            currentWord += letter.lower()
    wordReturn.append(currentWord)
    return wordReturn


def readRSS(feeds, timeDisplayLimit):
    '''
     Gets data from several global news sites.
     Only looks at articles that have been in the last few days based on
     timeDisplayLimit
     Display all feeds, set timeDisplayLimit = None
     Also note, this removes the timezone information, because RSS feeds tend
     not to standardize this.
     '''
    news = []
    for feed in feeds:
        d = feedparser.parse(feed)
        for entry in d['entries']:
            published = entry.get('published')
            if published is not None and timeDisplayLimit is not None:
                # have this in case there isn't a published field in the data.
                published = published.replace(',', '')
                published = published.replace(' +0000', '')
                published = published.replace(' -0500', '')
                published = published.replace(' -0400', '')
                published = published.replace(' EST', '')
                published = published.replace(' EDT', '')
                published = published.replace(' GMT', '')
                published = datetime.strptime(published, "%a %d %b %Y %X")
                lastWeek = datetime.today() - timedelta(days=timeDisplayLimit)
                if lastWeek < published:
                    news.append(entry)
            else:
                news.append(entry)
    return news


def display_my_results(goodText, badText, feeds, timeDisplayLimit=7):
    '''
    This is the "main" method...
    Call this method to receive a list of news articles.
    @timeDisplayLimit is the number of days to display the data.
    This only works if the publication date exists in the RSS feed
    (not always the case).
    '''
    goodText = parseText(goodText)
    badText = parseText(badText)
    feedResults = readRSS(feeds, timeDisplayLimit)
    resultsArray = []
    for article in feedResults:
        detail = article.get('summary_detail', 0).get('value')
        resultsArray.append(article.get('title') + detail)
    sortedNewsArray = analyzeText(goodText, badText, resultsArray, feedResults)
    return sortedNewsArray

def cleanData(words):
    '''
    This method filters through data to prepare it to be written to MongoDB
    '''
    return filter(lambda x: x in string.printable, words) + '/n'


def upArticle(data, dbId):
    '''
    This method writes an article to MongoDB indicating that it should be
    included in the "good text" analysis.
    '''
    string = cleanData(data)
    wordRecord = g.mongo.db.wordBank.find_one({'name': dbId})
    if wordRecord is not None:
        wordRecord['data'] = wordRecord.get('data') + string
        g.mongo.db.wordBank.save(wordRecord)


def downArticle(data, dbId):
    '''
    This method writes an article to MongoDB indicating that it should be
    included in the "bad text" analysis.
    '''
    string = cleanData(data)
    wordRecord = g.mongo.db.wordBank.find_one({'name': dbId})
    if wordRecord is not None:
        wordRecord['data'] = wordRecord.get('data') + '/n'+string
        g.mongo.db.wordBank.save(wordRecord)
