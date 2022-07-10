'''This Program is for tweepy authorization'''
import tweepy
import twitter_credentials

class Twitter_authenticator:
    def get_authenticate():
     
        auth=tweepy.OAuthHandler(twitter_credentials.Api_key,twitter_credentials.Api_key_secret)
        auth.set_access_token(twitter_credentials.access_token,twitter_credentials.access_token_secret)
        return auth