#Module provides 2 Functions:
# 1) getResults creates dictionary of users, and calls calc_score to retrieve results
# 2) calc_score fetches data from Twitter, runs Google NLP, and returns a raw score
#    for each handle as well as the most positive and negative tweets

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#Imports Tweepy 
import tweepy

#import credentials from config.py
from config import consumer_key, consumer_secret, access_key, access_secret

#Creates a dictionary from handles, runs calc_score on each handle, and returns list of dictionaries
def getResults(api, client, userlist, tweetnumber = 10):

    #create list of dictionaries to store attributes
    outputlist = []
    for user in userlist:
        userdict =  {"handle": "", "score": 0, "mostpos": "", "mostneg": ""}
        userdict["handle"] = str(user)
        outputlist.append(userdict)

    #iterate through coach list and fetch scores
    for user in outputlist:
        (user["score"], user["mostpos"], user["mostneg"]) = calc_score(client=client, api=api, handle=user["handle"], tweetcount = tweetnumber)
    
    #sort list by score
    outputlist.sort(key=lambda x: x['score'])
    return outputlist


#App Engine -- Retrieves data from twitter and runs NLP. Returns total score and most positive/negative 
# tweets
def calc_score(api, client, handle, tweetcount = 10):

    #disallow retweets
    handle = handle + "-filter:retweets"

    #Vars encapsulating key attributes of each handle:
    rawscore = 0 #Raw score for handle
    mostpos = "" #most positive tweek
    mpscore = -100000 #associated score for most positive tweet
    mostneg = "" #most negative tweet
    mnscore = 100000 #associated score for most negative tweet
    
    #Request n tweets for query
    tweets = api.search(q = handle,count=tweetcount)
    
    #Iterate through tweets and process
    for tweet in tweets:

        #Extract text
        text = tweet.text 

        #Perform NLP processing
        document = types.Document(content=text,type=enums.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(document=document).document_sentiment

        #calc score and add to raw score
        score = sentiment.score * sentiment.magnitude
        rawscore += score

        #update most postive and most negative tweets
        if score > mpscore:
            mpscore = score
            mostpos = text.strip()
        if score < mnscore:
            mnscore = score
            mostneg = text.strip()

    return (rawscore, mostpos, mostneg)


    

