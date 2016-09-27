__author__ = 'kapish'
from secrets import Oauth_Secrets
import tweepy
from tweepy import OAuthHandler

def primary(input_hashtag):
    s_auth(input_hashtag)

def s_auth(input_hashtag):
    secrets = Oauth_Secrets()
    auth = OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)