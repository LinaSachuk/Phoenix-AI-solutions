from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials


class TwitterStreamer():
    '''
    Class fir streaming and processing live tweets
    '''

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authentication and the connection to the Twitter Streamming API
        listener = StdOutListener()
        auth = OAuthHandler(twitter_credentials.API_key,
                            twitter_credentials.API_key_secret)
        auth.set_access_token(twitter_credentials.Access_token,
                              twitter_credentials.Access_token_secret)

        stream = Stream(auth, listener)

        stream.filter(track=hash_tag_list)


class StdOutListener(StreamListener):
    '''
    This is a basic listener class that just prints received tweets to stdout
    '''

    def init(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print('Error on_data: %s' % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":

    hash_tag_list = ['donald trump', 'barack obama']
    fetched_tweets_filename = 'tweets.json'

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
