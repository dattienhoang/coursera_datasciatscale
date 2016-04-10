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
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    #the following will go into main

    # this will actually be inputted with the sys.argv...rectify later
    #files = [
    #'output.txt'
    #]
    files = [sys.argv[2]]#[tweet_file]
    
    #f = open('problem_1_submission.txt','w')
    #ct = 0
    twdat = []
    for file in range(len(files)):
        tws = open(files[file], 'r')
        #print tws
        for line in tws:
            try:
                tweet = json.loads(line)
                twdat.append(tweet)
                #if ct < 20:
                #    f.write(line) # python will convert \n to os.linesep
                #    ct += 1
            except:
                continue
    #print '...total number of tweets:', len(twdat)
    #f.close() # you can omit in most cases as the destructor will call it
    #print '...searching for incomplete tweet entries'
    #print len(twdat)
    excise = []
    for iline in range(len(twdat)):
        #print iline
        if 'text' not in twdat[iline]:
            excise.append(iline)
    if len(excise) != 0:
        twdat = [i for j, i in enumerate(twdat) if j not in excise]
        #print '......incomplete tweets found and excised!'
    #print len(excise)
    #print '...total number of tweets:', len(twdat)
    #now extract portion w/ tweet
    #cant use pandas....!!! >_<
    #tweets = pd.DataFrame()
    #tweets['text'] = map(lambda tweet: tweet['text'].encode('utf-8', errors='replace'), twdat)
    #clear from memory
    #del twdat, excise, tws, tweet
    tweets = []
    tweets = map(lambda tweet: tweet['text'].encode('utf-8', errors='replace'), twdat)
    #for i in tweets: print i
    #print len(tweets)
    
    #load the affinities file...will actually be called with the whole script...rectify later...
    #afinnfile = open("AFINN-111.txt")
    afinnfile = open(sys.argv[1])#sent_file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    #print '...vomiting affinities list:'
    #print scores.items() # Print every (term, score) pair in the dictionary
    #print (scores.keys())[0]
    
    #now go through each tweet and print the sentiment score of each tweet!
    #for i in tweets:
    twscore = []
    val = 0
    for tweet in tweets:#['text']:
        for key in scores:
            #print key
            #print scores[key]
            val2 = tweet.find(key)
            if val2 != -1: val += scores[key]
            #print val
        twscore.append(val)
        val = 0
    #print twscore
    #print len(twscore)
    for scorei in range(len(twscore)): print (twscore[scorei])

if __name__ == '__main__':
    main()
