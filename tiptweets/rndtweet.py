import twitter
import random
import os
import sys

'''
Tweets a random line from the tweets.txt file
If a number (x) is specified as the first param then there is a 1 in x chance of the tweet being sent.
This can be used to randomise the time a tweet is sent eg by running this script every hour specifying 24 -
on average one tweet will then be send per day.
'''
if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        rnd_int = int(sys.argv[1])
        if random.randint(1, rnd_int) > 1:
            print('1 in %i chance failed' % rnd_int)
            sys.exit()
        print('1 in %i chance succeeded' % rnd_int)
        
    total_ok = 0
    total_not = 0
    lines = []
    
    # Read file in
    with open('tweets.txt', 'r') as f:
      for l in f:
        if len(l) > 280:
          total_not += 1
          print('Line too long: ' + str(len(l)) + ': ' + l)
        elif len(l) > 0:
          total_ok += 1
          lines.append(l)
    
    api = twitter.Api(consumer_key = os.getenv('TWITTER_CONSUMER_KEY'),
                      consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET'),
                      access_token_key = os.getenv('TWITTER_ACCESS_TOKEN'),
                      access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
    
    tw = random.choice(lines)
    print('Tweeting: ' + tw)
    
    api.PostUpdate(tw)