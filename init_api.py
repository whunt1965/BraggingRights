#Module initializes Twitter API and Google NLP Client

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#Imports Tweepy
import tweepy

#Import credentials from config file
from config import consumer_key, consumer_secret, access_key, access_secret

def init_api():
    #authorize for Twitter and initialziation of Tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Instantiates GoogleNLP client
    client = language.LanguageServiceClient()
    return api, client