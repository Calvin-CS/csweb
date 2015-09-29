
'''
This class uses sklearn's Logistic Regression and text Vectorization methods
to analyze text and generate an array of sorted text based on a given "good text and bad text" learning data.

By uncommenting the lines that are commented out, Niave Bayes can be used instead of linear regression.
Created October 1, 2014
@author: dad32
'''
from __future__ import division
from functools import wraps
from decimal import *
import urllib2
from xml.dom import minidom, Node
import time
from datetime import datetime, timedelta, date
import numpy as np
#from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import string



'''
 Given the two word bags, this function uses numpy's Linear 
 Regression to get the statistics for the words.
 '''
def reCalcStats(textGood, textBad):
    #global nb
    global lr
    global vectorizer  
    target = []

    #create an array indicating good and bad words.
    for word in textBad:
        target.append(1)
        
    for word in textGood:
        target.append(0)    


    newTarget = np.array(target)
    vectorizer = CountVectorizer(min_df=1)
    
    #change the words into a bag of words format                 
    CountVectorizer(analyzer='word', binary=False,
            # charset=None, charset_error=None,     These are no longer supported. - kvlinden, Summer, 2015
            decode_error='strict',
            dtype='numpy.int64', encoding='utf-8', input='content',
            lowercase=True, max_df=1.0, max_features=None, min_df=1,
            ngram_range=(1, 1), preprocessor=None, stop_words=None,
            strip_accents=None, token_pattern='(?u)\\b\\w\\w+\\b',
            tokenizer=None, vocabulary=None)
    
    vectorizedWords = vectorizer.fit_transform(textBad + textGood)
    arrayFormat = vectorizedWords.toarray()


    '''#n bays
    nb = GaussianNB()
    nb.fit(arrayFormat,newTarget)'''

    #LogisticRegressionn
    lr = LogisticRegression()
    lr.fit(arrayFormat,newTarget)



'''
 This method organizes the input into a sorted array of how good each input array item is 
 to the given logestic regression analysis that has already been performed.
'''
def predictWords(inputArray,dictItem):
    #global nb
    global lr
    global vectorizer
    
    predictionArray = []

    
    newInputArray = vectorizer.transform(inputArray).toarray()
    #nbPrediction = nb.predict(newInputArray)
    lrPrediction = lr.predict(newInputArray)
    
    i = 0
    for article in inputArray:
        predictionArray.append(lr.predict_log_proba(newInputArray[i])[0][0]*-1)
        i= i+1
    
    ''' Sample test data
    words = ['the','and', 'I', 'that','is','has', 'Internet','it','to', 'to it','security Internet learn','learn', 'calvin','hope','calvin it is knights','hope it is knights','it is knights']  
    input = vectorizer.transform(words).toarray()
    i = 0
    for word in input:
        print words[i]
        predictionArray.append(lr.predict_log_proba(word)[0][0]*-1)
        print lr.predict_log_proba(word)[0][0] * -1

        print "NB Prediction: " + str(nb.predict_log_proba(word)[0] * -1)

        print "LR Prediction: " + str(lr.predict_log_proba(word)[0] * -1)
        i = i+1
    '''
        
    #Now we merge the array of news articles based on the ranking it received from the associated ranking array above
    yx = zip(predictionArray,dictItem)
    yx.sort()
    x_sorted = [dictItem for predictionArray, dictItem in yx]
    return x_sorted 



'''
Given an array of words, good, bad, and new ones to sort
this method uses logestic regression to sort the words.
'''
def analyzeText(goodText, badText, analyzeInput,dictItem=False):
    if dictItem is False:
        dictItem = analyzeInput
    reCalcStats(goodText,badText)
    newsArray =predictWords(analyzeInput, dictItem)
    return newsArray

