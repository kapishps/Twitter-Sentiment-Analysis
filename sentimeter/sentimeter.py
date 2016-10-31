__author__ = 'kapish'
from secrets import Oauth_Secrets
import tweepy
from textblob import TextBlob

def primary(input_hashtag):
    secrets = Oauth_Secrets()       #secrets imported from secrets.py
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)

    api = tweepy.API(auth)

    N = 100                         #Number of Tweets
    Tweets = tweepy.Cursor(api.search, q=input_hashtag).items(N)
    neg=0.0
    n=0.0
    net=0.0
    pos=0.0
    p=0.0
    for tweet in Tweets:
        print tweet.text
        blob = TextBlob(tweet.text)
        if blob.sentiment.polarity < 0:         #Negative
            neg+=blob.sentiment.polarity
            n+=1
        elif blob.sentiment.polarity == 0:      #Neutral
            net+=1
        else:                                   #Positive
            pos+=blob.sentiment.polarity
            p+=1
    print "Total tweets",N
    print "Positive ",float(p/N)*100,"%"
    print "Negative ",float(n/N)*100,"%"
    print "Neutral ",float(net/N)*100,"%"