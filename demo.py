import tweepy
from textblob import TextBlob

consumer_key = 'kVmGSnXxOqZbE4NkJM5xxXH0c' 
consumer_secret = 'UiFY5oIgPaaJ5bX3C5b7AFqUDSPYcVhRDua7lw1WmRoIM1vycw'

access_token = '1114013036069527552-p7aBhtEFkb8mDx7nch21pA36TC0V4P'
acces_token_secret = 'gcTUIY8dHxgjrEFfqxwvb4SqADRO68qHnUD1jBjhUwhgX'

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

