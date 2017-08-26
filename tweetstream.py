import tweepy
import json

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from config import *
import sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()


non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

# Variables that contains the user credentials to access Twitter API 
##access_token = "INSERT ACCESS TOKEN"
##access_token_secret = "INSERT ACCESS TOKEN SECRET"
##consumer_key = "INSERT CONSUMER KEY"
##consumer_secret = "INSERT CONSUMER SECRET"

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
##        print (data["text"])
        dictData = json.loads(data)
        text = dictData["text"].translate(non_bmp_map)
        print(text)
        print(sid.polarity_scores(text))
##        print(data)
        return True

    def on_error(self, status):
        print("s")
        print (status)


if __name__ == '__main__':
    # This handles Twitter authentication and connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    stream = Stream(auth, l)    
    api = tweepy.API(auth)
    api.send_direct_message(screen_name = "AdvaitMaybhate", text="Hi")
    stream.filter(follow=[api.get_user("normanamadison").id_str])
