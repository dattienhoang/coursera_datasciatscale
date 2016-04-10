import json
import sys

#def hw():
#    print 'Hello, world!'
#
#def lines(fp):
#    print str(len(fp.readlines()))
#
#def main():
#    sent_file = open(sys.argv[1])
#    tweet_file = open(sys.argv[2])
#
#if __name__ == '__main__':
#    main()

    #the following will go into main

    # this will actually be inputted with the sys.argv...rectify later
    files = [
    'output.txt'
    ]
    #files = [sys.argv[2]]

    twdat = []
    for file in range(len(files)):
        tws = open(files[file], 'r')
        #print tws
        for line in tws:
            try:
                tweet = json.loads(line)
                twdat.append(tweet)
            except:
                continue
    print '...total number of tweets:', len(twdat)
    print '...searching for incomplete tweet entries'
    print len(twdat)
    excise = []
    for iline in range(len(twdat)):
        if 'text' not in twdat[iline]:
            excise.append(iline)
    if len(excise) != 0:
        twdat = [i for j, i in enumerate(twdat) if j not in excise]
        print '......incomplete tweets found and excised!'
    print len(excise)
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

newterms = {}
for tweet in tweets['text']:
    #separate each word in text already
    uniqwrds = tweet.split()
    #pop out strings in tweet that are already in affinities library...
    for i in range(len(uniqwrds)):
        topop = []
        if uniqwrds[i] in scores: topop.append(i)
    uniq = uniqwrds.pop(topop)
        
