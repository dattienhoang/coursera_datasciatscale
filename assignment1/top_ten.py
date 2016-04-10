# -*- coding: utf-8 -*-
"""
Created on Mon Nov 02 11:46:01 2015

@author: Dat Tien Hoang

Notes:
when calling this program, two inputs are needed:
(1) a sentiment file
(2) a file of tweets
they should be called in the following order:
python tweet_sentiment.py <sent>.txt <data>.txt > <result>.txt
"""



import json
import sys
## import pandas as pd

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))#

def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    
    # this will actually be inputted with the sys.argv...rectify later
    #files = [#'three_minutes_tweets.json'
    #'output.txt'
    #]
    files = [sys.argv[1]]#[tweet_file]
    
    twdat = []
    for file in range(len(files)):
        tws = open(files[file], 'r')
        for line in tws:
            try:
                tweet = json.loads(line)
                twdat.append(tweet)
            except:
                continue
    excise = []
    for iline in range(len(twdat)):
        if 'text' not in twdat[iline]:
            excise.append(iline)
    if len(excise) != 0:
        twdat = [i for j, i in enumerate(twdat) if j not in excise]
    #now extract portion w/ tweet
    tweets = []
    tweets = map(lambda tweet: (tweet['entities']['hashtags']), twdat)
    #each tweet has a list of hashtags...what we just mapped is still a list
    #join it al into a string
    excise = []
    for iline in range(len(tweets)):
        if len(tweets[iline]) == 0:
            excise.append(iline)
    if len(excise) != 0:
        tweets = [i for j, i in enumerate(tweets) if j not in excise]
    #print tweets
    hashs = []
    for i in range(len(tweets)):
        #print (tweets[i])#[0]
        for htaginfo in tweets[i]:
            #print htaginfo
            #print htaginfo.values()
            hashs.append((htaginfo.values())[1].encode('utf-8', errors='replace'))
            #print (tweets[i])[0][u'text'].encode('utf-8', errors='replace')
            #hashs.append( (tweets[i])[0][u'text'].encode('utf-8', errors='replace'))
    #print hashs
    #alltxt = hashs
    for i in range(len(hashs)):
        if i == 0:
            alltxt = hashs[i]
        else:
            alltxt += ' ' + hashs[i]
    #now combine all the tweets into one string and sort into a dictionary
    txthist = dict((x, (alltxt.split()).count(x)) for x in alltxt.split())
    #nterms = float(len(alltxt.split()))
    hashn = 0
    for w in sorted(txthist, key=txthist.get, reverse=True):
        if hashn <= 9:
            print w, txthist[w]#/float(nterms)
            hashn += 1
    
    #hashn = 0
    #for key, value in txthist.iteritems():
    #    if hashn <= 9:
    #        print key, value/nterms
    #        hashn += 1

if __name__ == '__main__':
    main()
