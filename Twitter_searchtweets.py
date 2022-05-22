import tweepy
from textblob import TextBlob
import re
import pandas as pd
import numpy as np
import Twitter_authetication


'''Class to analyze tweets of a topic'''
class Twitter_Sentiment_search_tweet:
 
  def __init__(self):
      self.auth=Twitter_authetication.Twitter_authenticator.get_authenticate()
      self.api=tweepy.API(auth=self.auth)

  def get_tweets(self,search_item):
      tweets=[]

      for tweet in tweepy.Cursor(self.api.search_tweets,q=search_item+" -filter:retweets",lang="en").items(200):
          tweets.append(tweet)
      return tweets


  def clean_tweet(self, tweet):
        
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


  def get_tweet_sentiment(self,tweet):
        analysis=TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity> 0:
            return "positive"
        elif analysis.sentiment.polarity==0:
            return "neutral"
        else:
            return "negative"

  def tweet_to_frame(self,tweets):
        df=pd.DataFrame(data=[self.clean_tweet(tweet.text) for tweet in tweets],columns=['Tweets'])
        df['ID']=np.array([tweet.id for tweet in tweets])
        df['Len']=np.array([len(tweet.text) for tweet in tweets])
        df['Date']=np.array([tweet.created_at for tweet in tweets])
        df['Source']=np.array([tweet.source for tweet in tweets])
        df['Sentiment']=np.array([self.get_tweet_sentiment(tweet) for tweet in df['Tweets']])
        return df

