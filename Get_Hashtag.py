import tweepy
import pymongo
from pymongo import MongoClient
client = MongoClient()

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

client = MongoClient('localhost', 27017)
db = client['scrapped_tweets_fin']
tweets = db.tweets



MAX_TWEETS = 5000
count=0

for tweet in tweepy.Cursor(api.search, q='#blacklivesmatter', rpp=100).items(MAX_TWEETS):
    print(tweet)
    result = tweets.insert_one(tweet._json)
    print('One post: {0}'.format(result.inserted_id))
    count=count+1
    print(count)
print("done")




