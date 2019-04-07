import tweepy
from textblob import TextBlob
import config

import numpy as np
import operator


consumer_key = config.consumerKey 
consumer_secret = config.consumerSecret

access_token = config.accessToken
acces_token_secret = config.accesTokenSecret


#user auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_token_secret)

api = tweepy.API(auth)

#List of Subjects
subjects_to_search = ['Trump', 'Elizabeth Warren', 'Bernie Sanders','Ocasio-Cortez', 'Joe Biden']
#Hashtag to search
hashtag = 'border wall'

#Date Ranges
since_date = '2019-01-01'
until_date = '2019-04-06'

#Labeling Analysis
def get_label(analysis, threshold = 0):
    if analysis.sentiment[0]>threshold:
        return 'Postive'
    else:
        return 'Negative'

#uses tweepy to access twitter api
all_polarities= dict()

for subject in subjects_to_search:
    this_subject_polarities = []

    this_subject_tweets = api.search(q=[hashtag, subject], count = 50, since = since_date, until = until_date)
    #saves to csv file
    with open('%s_tweets.csv' % subject, 'w') as this_subject_file:
        this_subject_file.write('tweet, sentiment_label\n')
        for tweet in this_subject_tweets:
            analysis = TextBlob(tweet.text)
            #Getting label corresponding to the sentiment analysis
            this_subject_polarities.append(analysis.sentiment[0])
            this_subject_file.write('%s, %s\n' % (tweet.text.encode('utf8'), get_label(analysis)))
    #Saves mean for final results
    all_polarities[subject] = np.mean(this_subject_polarities)

#printing result
sorted_analysis = sorted(all_polarities.items(), key=operator.itemgetter(1), reverse=True)
print ('Mean Sentiment Polarity in decending order : ')
for subject, polarity in sorted_analysis:
    print ('%s : %0.3f' % (subject, polarity))

# Mean Sentiment Polarity in decending order :
# Ocasio-Cortez : 0.210
# Trump : 0.116
# Elizabeth Warren : 0.096
# Joe Biden : 0.048
# Bernie Sanders : 0.018