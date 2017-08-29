
def sendMessages(msg):
    if fuzz.token_set_ratio("hello hi", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="Hey!")
    
    if fuzz.token_set_ratio("hurt myself", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="I'm sorry you're in so much pain. I won't leave you or abandon you.")

    elif fuzz.token_set_ratio("pain hurt inside", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="You’re not alone in this. We're here for you.")

    elif fuzz.token_set_ratio("I love cats!", msg['direct_message']['text']) > 60:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text=list(giphypop.Giphy().search("cats"))[0])
    
    elif fuzz.token_set_ratio("distance from friends family", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="Keep yourself united with your loved ones. They will always be there to help you.")

    elif fuzz.token_set_ratio("avoid everything isolation", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="Come out into the sunshine! The world is much better with you in it :)")

    elif fuzz.token_set_ratio("agony makes me insane", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="Do you want a hug? I will always be here for you")

    elif fuzz.token_set_ratio("exhuasting battle", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="You'll make it through!")

    elif fuzz.token_set_ratio("eat less starve", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="Keep yourself well. You derseve it. You are the best person I know.")

    elif fuzz.token_set_ratio("procrastinate", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="I know how much you want to curl away from the world, but I'll be there with you every step of the way.")

    elif fuzz.token_set_ratio("empty and hopeless", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="I know life may seem hopeless now, but you will get through it.")

    elif fuzz.token_set_ratio("frustration and anger", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="You're not going crazy. Stay strong, I believe in you.")

    elif fuzz.token_set_ratio("anxious and restless", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="We are not on this earth to see through one another, but to see one another through.")

    elif fuzz.token_set_ratio("worthless and guilt", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="You deserve the world. You mean everything to me. I <3 you")

    elif fuzz.token_set_ratio("back pain and headaches", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="Stay strong. These pains will pass, and I will help you through them.")

    elif fuzz.token_set_ratio("can't get out of bed", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="You can survive this. When all this is over, I’ll still be here and so will you.")

    elif fuzz.token_set_ratio("fatigue and tired", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="Even if it doesn't seem that way now, this feeling will not last forever.")

    elif fuzz.token_set_ratio("can't think", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="I might not always be able to to understand, but I offer my compassion")

    elif fuzz.token_set_ratio("can't sleep", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="Just breathe, relax. Think of something peaceful and positive. You'll make it through this.")

    elif fuzz.token_set_ratio("kill myself", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="DONT KILL YOURSELF THERE'S TOO MUCH TO LIVE FOR!")

    elif fuzz.token_set_ratio("Nothing good in life", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="Take pride in your small victories, because they lead to bigger ones.")

    elif fuzz.token_set_ratio("depressed", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="You're not wrong for feeling the way you do and no one blames you for it.")

    elif fuzz.token_set_ratio("sad", msg['direct_message']['text']) > 50:
        twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="I won't always know how you feel, but I care about you")
    



















from twitter import *
import os

import oauth
import tweepy
from tweepy import OAuthHandler
import config
from fuzzywuzzy import fuzz
from pymongo import MongoClient
import giphypop
##import tweetstream as ts

#Create a new Twitter app first: https://apps.twitter.com/app/new
auth=OAuth(config.access_key, config.access_secret, config.consumer_key, config.consumer_secret)
twitter_api = Twitter(auth=auth)
twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')
print("here")


authi = OAuthHandler(config.consumer_key, config.consumer_secret)
authi.set_access_token(config.access_key, config.access_secret)
api = tweepy.API(authi)
client = MongoClient()
db = client["node-login"]
cursor = db.accounts
##print(type(cursor.find_one({"handle":"therapyChatBot"})))
##print(cursor.find_one("handle":msg['direct_message']['sender']['screen_name']))

followers = list(map(str,list(tweepy.Cursor(api.followers_ids, screen_name="TherapyChatBot").pages())[0]))
print(followers)
##print(twitter_api.followers_ids)
import subprocess as sp

extProc = sp.Popen(['python','tweetstream.py', ",".join(followers)]) # runs myPyScript.py 

status = sp.Popen.poll(extProc) # status should be 'None'
print(status)

for msg in twitter_userstream.user():
    try:
        if msg["event"] == "follow":
            print("followed")
            print(msg["source"]["screen_name"])
            sp.Popen.terminate(extProc) # closes the process
            followers = list(map(str,list(tweepy.Cursor(api.followers_ids, screen_name="TherapyChatBot").pages())[0]))
            print(followers)
            status = sp.Popen.poll(extProc) # status should now be something other than 'None' ('1' in my testing)
            extProc = sp.Popen(['python','tweetstream.py', ",".join(followers)]) # runs myPyScript.py 
    except KeyError:
        pass
    
    if 'direct_message' in msg:
        if msg['direct_message']['sender']['screen_name'] != "TherapyChatBot":
            sendMessages(msg)
            print (msg['direct_message']['text'])
##print("past")






























































































            
