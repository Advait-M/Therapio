from twitter import *
import os

import oauth
import config
from fuzzywuzzy import fuzz

#Create a new Twitter app first: https://apps.twitter.com/app/new


##APP_KEY,APP_SECRET = 'H3kQtN5PQgRiA0ocRCCjqjt2P', '51UaJFdEally81B7ZXjGHkDoDKTYy430yd1Cb0St5Hb1BVcDfE'
# OAUTH_TOKEN, OAUTH_TOKEN_SECRET = '149655407-TyUPMYjQ8VyLNY5p7jq0aMy8PjtFtd7zkIpDh3ZA', 'IUVpiDpoVmdO75UaHOTinAv5TOsAQmddttNENh9ofYuWO'


##MY_TWITTER_CREDS = os.path.expanduser('my_app_credentials')
##if not os.path.exists(MY_TWITTER_CREDS):
##    oauth_dance("crypto sentiments", APP_KEY, APP_SECRET,
##                MY_TWITTER_CREDS)

##oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
#
#twitter = Twitter(
##auth=OAuth(config.access_key, config.access_secret, config.consumer_key, config.consumer_secret))
auth=OAuth(config.access_key, config.access_secret, config.consumer_key, config.consumer_secret)
twitter_api = Twitter(auth=auth)
twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')
print("here")
    
for msg in twitter_userstream.user():
##    print("h")
##    print(msg)
    if 'direct_message' in msg:
        if msg['direct_message']['sender']['screen_name'] != "TherapyChatBot":
##            print(fuzz.token_set_ratio("kill myself", msg['direct_message']['text']))
            if fuzz.token_set_ratio("kill myself", msg['direct_message']['text']) > 50:
                twitter_api.direct_messages.new(user=msg['direct_message']['sender']['screen_name'], text="DONT KILL YOURSELF THERE'S TOO MUCH TO LIVE FOR!")
            print (msg['direct_message']['text'])
##print("past")
        

    
