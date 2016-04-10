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

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))#

def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    #the following will go into main
    
    # this will actually be inputted with the sys.argv...rectify later
    #files = [
    #'output.txt'
    #]
    files = [sys.argv[2]]
    
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
    excise = []
    for iline in range(len(twdat)):
        if 'text' not in twdat[iline]:
            excise.append(iline)
    if len(excise) != 0:
        twdat = [i for j, i in enumerate(twdat) if j not in excise]
    tweets = map(lambda tweet: tweet['text'].encode('utf-8', errors='replace'), twdat)
    locdat = map(lambda tweet: tweet['place'], twdat)
    stres = []
    for i in locdat:
        #print i
        if i is None: stres.append(None)
        else:
            #print i['full_name'].encode('utf-8', errors='replace')
            for state in states:
                foundst = (i['full_name'].encode('utf-8', errors='replace')).find(' '+state)
                if foundst != -1: stres.append(state)
            if foundst == -1: stres.append(None)
    #print stres
    
    #intitialize a dictionary to hold all the happiness scores of states
    stscore = dict((x, 0) for x in states.keys())
    #print stscore
    
    #load the affinities file...will actually be called with the whole script...rectify later...
    #afinnfile = open("AFINN-111.txt")
    afinnfile = open(sys.argv[1])#sent_file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.
    
    #now go through each tweet and print the sentiment score of each tweet!
    #for i in tweets:
    twscore = []
    val = 0
    for tweet in tweets:#['text']:
        for key in scores:
            val2 = tweet.find(key)
            if val2 != -1: val += scores[key]
        twscore.append(val)
        val = 0
    #choose tweets with a not none type entry for state, and add that tweet sentiment to states score
    for i in range(len(tweets)):
        if stres[i] is not None:
            stscore[stres[i]] += twscore[i]
    #print stscore
    print (sorted(stscore, key=stscore.get, reverse=True))[0]

if __name__ == '__main__':
    main()
