import tweepy
from textblob import TextBlob
import config

consumer_key = config.consumerKey 
consumer_secret = config.consumerSecret

access_token = config.accessToken
acces_token_secret = config.accesTokenSecret


#user auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_token_secret)

api = tweepy.API(auth)

#api call
public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

