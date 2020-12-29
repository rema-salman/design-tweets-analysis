# Libraries
from decouple import config
import tweepy

# Variables of the user credentials to access Twitter API
consumer_key = config('CONSUMER_KEY')
consumer_secret = config('CONSUMER_SECRET')
access_token = config('ACCESS_TOKEN')
access_token_secret = config('ACCESS_TOKEN_SECRET')


class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # Save streamed tweet to json file, and hash tag for sorting the data
        # Authenticate using config.py and connect to Twitter Streaming API.
        listener = TwitterListener(fetched_tweets_filename)
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        stream = tweepy.Stream(auth, listener)
        # Filter Twitter Streams to capture data by the keywords, and only english language
        stream.filter(track=hash_tag_list, languages=["en"])

    def main(self):
        hash_tag_list = ['design', 'user experience',
                         'design vs art']  #create keywords list
        fetched_tweets_filename = "fetched_tweets.txt"
        # Invokes the streaming to collect tweets
        self.twitter_streamer.stream_tweets(fetched_tweets_filename,
                                            hash_tag_list)


class TwitterListener(tweepy.StreamListener):
    """
    Basic listener class: recived tweets to standard out
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
        self.counter = 0
        self.tweets_count = 3000


    # saves the fetched tweets into a file until reaching the specified count(3000)
    def on_data(self, data):
        try:
            # open the file and appande (to keep adding tweets, instead of re-writting)
            with open(self.fetched_tweets_filename, 'a+') as tf:
                tf.write(data)
            if self.counter < self.tweets_count:
                self.counter += 1
                return True
            else:
                tf.close()
                print("DONE!")
                return False
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True


    # Returning False on_data method in case rate limit occurs.
    def on_error(self, status):
        if status == 420:
            return False
        print(status)
