import tweepy
import pandas as pd
import os

bearer_token = os.getenv("X_BEARER")

if not bearer_token:
    raise ValueError("Environment variable 'X_BEARER' not set")

client = tweepy.Client(bearer_token)

query = "IHSG Anjlok -is:retweet lang:id"
tweets = client.search_recent_tweets(query=query, tweet_fields=["created_at", "author_id", "text"], max_results=100)

if tweets.data:
    df = pd.DataFrame([t.data for t in tweets.data])
    df.to_csv("tweets.csv", index=False, encoding="utf-8-sig")
    print("Saved to tweets.csv")
else:
    print("No tweets found.")
