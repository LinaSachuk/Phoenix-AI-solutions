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
# api = API(auth)

# # The search term you want to find
# query = "Tesla"

# # Language code (follows ISO 639-1 standards)
# language = "en"

# # The numbers of tweets per page, up to 100
# count = 100

# # Calling the user_timeline function with our parameters
# results = api.search(q=query, lang=language, count=count)


# counter = 0

# # foreach through all tweets pulled
# for tweet in results:
#     print(tweet)
#     # printing the text stored inside the tweet object
#     print(tweet.user.screen_name, "Tweeted:",
#           tweet.text)
#     counter += 1

#     print('count: ============= ', counter)


# API.search_30_day(environment_name, query[, tag][, fromDate][, toDate][, maxResults][, next])
api = API(auth)

# environment_name  - The (case-sensitive) label associated with your search developer environment
environment_name = 'dev'


# The search term you want to find
query = "Tesla"

# If neither the fromDate or toDate parameter is used, the API will deliver all results for the most recent 30 days, starting at the time of the request, going backwards.

# maxResults – The maximum number of search results to be returned by a request. A number between 10 and the system limit (currently 500, 100 for Sandbox environments). By default, a request response will return 100 results.
maxResults = 100

# Calling the user_timeline function with our parameters
results = api.search(environment_name=environment_name,
                     q=query)


counter = 0

# foreach through all tweets pulled
for tweet in results:
    print(tweet)
    # printing the text stored inside the tweet object
    print(tweet.user.screen_name, "Tweeted:",
          tweet.text)
    counter += 1

    print('counter: ============= ', counter)
