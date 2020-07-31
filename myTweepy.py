from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


from textblob import TextBlob

import twitter_credentials

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

# # # # TWITTER AUTHENTICATOR # # # #
# Creating the authentication object
auth = OAuthHandler(twitter_credentials.API_key,
                    twitter_credentials.API_key_secret)

# Setting your access token and secret
auth.set_access_token(twitter_credentials.Access_token,
                      twitter_credentials.Access_token_secret)

# ======================search methods===========================


# # API.search(q[, geocode][, lang][, locale][, result_type][, count][, until][, since_id][, max_id][, include_entities])
# # Creating the API object while passing in auth information
api = API(auth)

# # The search term you want to find
query = "Tesla"

# # Language code (follows ISO 639-1 standards)
language = "en"

# # The numbers of tweets per page, up to 100
count = 100

# # Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language, count=count)


counter = 0

# foreach through all tweets pulled
for tweet in results:
    print(tweet)
    # printing the text stored inside the tweet object
    print(tweet.user.screen_name, "Tweeted:",
          tweet.text)
    counter += 1

    print('count: ============= ', counter)


# Flattening Twitter JSON
tweet_list = []
with open('all_tweets.json', 'r') as fh:
    tweets_json = fh.read().split("\n")

    for tweet in tweets_json:
        tweet_obj = json.loads(tweet)

        if 'extended_tweet' in tweet_obj:
            tweet_obj['extended_tweet-full_text'] = tweet_obj['extended_tweet']['full_text']

    tweet_list.append(tweet)

tweets_df = pd.DataFrame(tweet_list)
