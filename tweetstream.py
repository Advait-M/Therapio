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
import pymongo
from googleplaces import GooglePlaces, types, lang
google_places = GooglePlaces(google_key)
sid = SentimentIntensityAnalyzer()
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
bot_handle = "TherapyChatBot"

class StdOutListener(StreamListener):
    def on_direct_message(self, status):
        print(status)
        author = status.author.screen_name
        api.send_direct_message(screen_name=author, text='response')

        return True
    
    def on_data(self, data):
        dictData = json.loads(data)
        print(dictData)
        text = dictData["text"].translate(non_bmp_map)
        user = dictData["user"]["name"].translate(non_bmp_map)
        print(user)
        print(text)
        for item in sid.polarity_scores(text):
            print(item + ": " + str(sid.polarity_scores(text)[item]))
        sentiment_score = sid.polarity_scores(text)["pos"] - sid.polarity_scores(text)["neg"]
        if (sentiment_score < 0):
            api.send_direct_message(screen_name = dictData["user"]["screen_name"], text="You need help.")
            print("help message was sent")
        else:
            print("help message was not sent")
        print("Sentiment score: %s" % (sentiment_score))
        return True

    def on_error(self, status):
        print("error")
        print (status)


l = StdOutListener()
auth = OAuthHandler(consumer_keya, consumer_secreta)
auth.set_access_token(access_keya, access_secreta)
stream = Stream(auth, l)    
api = tweepy.API(auth)

##followers = list(map(str,list(tweepy.Cursor(api.followers_ids, screen_name=bot_handle).pages())[0
import sys
followers = sys.argv[1].split(",")
print(followers)
print("Ready")

stream.filter(follow=followers)
    
