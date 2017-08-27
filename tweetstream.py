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

from pymongo import MongoClient
import sys
import giphypop
from random import randint

gif_search_params = ["cat","kitty","puppy","dog","baby"]
gif_list = list(giphypop.Giphy().search(gif_search_params[randint(0,len(gif_search_params)-1)]))

def nearbyDoctors(location):
    google_places = GooglePlaces(google_key)
    query_result = google_places.nearby_search(location=location, keyword='psychiatrist')
    counter = 1
    doctors = []
    for place in query_result.places:
        if "Dr" == place.name[0:2]:
            place.get_details()
            try:
                phone = place.local_phone_number
            except AttributeError:
                continue
            doctors += [str(counter) + ". Name: " + place.name, "Address: " + place.formatted_address, "Phone: " + phone]
            counter += 1
        if counter == 6:
            break
    return "\n".join(doctors) + "\nAccess on Google Maps: https://www.google.com/maps?q=nearby+psychiatrists"


##sys.stdout = open('C:\\Users\\advai\\Documents\\GitHub\\MentalHealthBot\\err.txt', 'w')
sys.stderr = open('C:\\Users\\advai\\Documents\\GitHub\\MentalHealthBot\\err.txt', 'w')

google_places = GooglePlaces(google_key)
sid = SentimentIntensityAnalyzer()
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
bot_handle = "TherapyChatBot"

client = MongoClient()
db = client["node-login"]
cursor = db.accounts

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
        user = dictData["user"]["screen_name"].translate(non_bmp_map)
        print(user)
        print(text)
##        input()
        for item in sid.polarity_scores(text):
            print(item + ": " + str(sid.polarity_scores(text)[item]))
        sentiment_score = sid.polarity_scores(text)["compound"]
        if (sentiment_score < 0):
            if (sentiment_score < -0.65):
                api.send_direct_message(screen_name = dictData["user"]["screen_name"], text='Is everything ok? Your recent post "' + text + '" is concerning. Please see your nearest psychiatrist for professional assistance as soon as possible.')
                
                result = cursor.find_one({"handle":user})
                print(result)
                if result != None:
                    api.send_direct_message(screen_name = dictData["user"]["screen_name"], text="Here's a list of nearby psychiatrists who can help you out:")
                
                    msg = nearbyDoctors(result["address"])
                    api.send_direct_message(screen_name = user, text=msg)
                    api.send_direct_message(screen_name = user, text="How are you feeling? What happened?")
                else:
                    print("User not found.")
            else:
                api.send_direct_message(screen_name = dictData["user"]["screen_name"], text='Is everything ok? Your recent post "' + text + '" is concerning. Take a look at this GIF to lighten your spirits.')
                api.send_direct_message(screen_name = dictData["user"]["screen_name"], text=gif_list[randint(0,len(gif_list)-1)])
##            api.send_direct_message(screen_name = dictData["user"]["screen_name"], text="You need help. http://24.media.tumblr.com/tumblr_m4g9kxA3Ip1qhwmnpo1_1280.jpg")
            print("Help message was sent")
        else:
            print("Help message was not sent")
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
    
