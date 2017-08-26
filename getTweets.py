from twitter import *
import time
import config

#Instance Twitter
twitter = Twitter(
auth=OAuth(config.access_key, config.access_secret, config.consumer_key, config.consumer_secret))

def getTweets(handle):
    print(handle)

    try:
        print("here")
        results = twitter.statuses.user_timeline(screen_name = handle)
        print("2")
        if results != []:

            # print(results)
            # print()

            statii = []

            #print(results)
            #print(results[0])

            uName = results[0]["user"]["name"]

            #print(uName)

            for status in results:
                statii.append(status["text"])

            print(statii)
            print(len(statii))
##            textS = " ".join(statii)
##            while "\n" in textS:
##                i = textS.index("\n")
##                textS = textS[0:i] + textS[i+1:]

            #print(textS)
            #print([uName, textS])

            return [uName, statii]
        else:
            return[]
    except TwitterHTTPError:
        return []
if __name__ == "__main__":
    politicallyActiveHandles = [
        "realDonaldTrump"]
    for i in politicallyActiveHandles:
        print(len(getTweets((i))[1]))
