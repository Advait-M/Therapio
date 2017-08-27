from twitter import *
import os

import oauth
import tweepy
from tweepy import OAuthHandler
import config
from fuzzywuzzy import fuzz
##import tweetstream as ts

#Create a new Twitter app first: https://apps.twitter.com/app/new
auth=OAuth(config.access_key, config.access_secret, config.consumer_key, config.consumer_secret)
twitter_api = Twitter(auth=auth)
twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')
print("here")


authi = OAuthHandler(config.consumer_key, config.consumer_secret)
authi.set_access_token(config.access_key, config.access_secret)
api = tweepy.API(authi)

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
            if fuzz.token_set_ratio("kill myself", msg['direct_message']['text']) > 50:
                twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="DONT KILL YOURSELF THERE'S TOO MUCH TO LIVE FOR!")
            print (msg['direct_message']['text'])
##print("past")
        

    
