import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['scrapped_tweets_fin']
tweets = db["tweets"]

file=open("tweets.txt","a",encoding="utf-8")

for tweet in tweets.find():
    print(tweet["text"])
    file.write("\n"+tweet["text"])

file.close()
