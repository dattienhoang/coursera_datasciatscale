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
# import pandas as pd

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))#

def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    
    # this will actually be inputted with the sys.argv...rectify later
    #files = ['problem_1_submission.txt'
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
    tweets = map(lambda tweet: tweet['text'].encode('utf-8', errors='replace'), twdat)
    
    #now combine all the tweets into one string and sort into a dictionary
    for i in range(len(tweets)):
        if i == 0:
            alltxt = tweets[i]
        else:
            alltxt += ' ' + tweets[i]
    txthist = dict((x, (alltxt.split()).count(x)) for x in alltxt.split())
    nterms = float(len(alltxt.split()))
    for key, value in txthist.iteritems():
        print key, value/nterms

if __name__ == '__main__':
    main()
