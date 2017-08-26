import tweepy
import json

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from config import *
import sys
import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
bot_handle = "TherapyChatBot"

class StdOutListener(StreamListener):

    def on_data(self, data):
        dictData = json.loads(data)
        text = dictData["text"].translate(non_bmp_map)
        user = dictData["user"]["name"].translate(non_bmp_map)
        print(user)
        print(text)
        for item in sid.polarity_scores(text):
            print(item + ": " + str(sid.polarity_scores(text)[item]))
        sentiment_score = sid.polarity_scores(text)["pos"] - sid.polarity_scores(text)["neg"]
        print("Sentiment score: %s" % (sentiment_score))
        if (sentiment_score < 0):
            api.send_direct_message(screen_name = dictData["user"]["screen_name"].translate(non_bmp_map), text="You need help.")
            print("help message was sent")
        else:
            print("help message was not sent")
        return True

    def on_error(self, status):
        print("error")
        print (status)


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    stream = Stream(auth, l)    
    api = tweepy.API(auth)
    
    followers = list(map(str,list(tweepy.Cursor(api.followers_ids, screen_name=bot_handle).pages())[0]))
    print("ready")
    stream.filter(follow=followers)
=======
    if (sentiment_score < 0):
        api.send_direct_message(screen_name = "AdvaitMaybhate", text="You need help.")
        print("help message was sent")
    else:
        print("help message was not sent")
