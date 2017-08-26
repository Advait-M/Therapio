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

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
##        print (data["text"])
        dictData = json.loads(data)
        text = dictData["text"].translate(non_bmp_map)
        user = dictData["user"]["name"].translate(non_bmp_map)
        print(user)
        print(text)
        for item in sid.polarity_scores(text):
            print(item + ": " + str(sid.polarity_scores(text)[item]))
        sentiment_score = str(sid.polarity_scores(text)["pos"] - sid.polarity_scores(text)["neg"])
        print(sentiment_score)
##        print(data)
        return True

    def on_error(self, status):
        print("error")
        print (status)


if __name__ == '__main__':
    # This handles Twitter authentication and connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    stream = Stream(auth, l)    
    api = tweepy.API(auth)
    followers = list(map(str,list(tweepy.Cursor(api.followers_ids, screen_name=bot_handle).pages())[0]))
    print("ready")
    stream.filter(follow=followers)
