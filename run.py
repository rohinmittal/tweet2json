# encoding=utf-8
from __future__ import unicode_literals
import streamClass

auth = streamClass.tweepy.OAuthHandler(streamClass._consumerToken, streamClass._consumerSecret)
auth.set_access_token(streamClass._accessToken, streamClass._accessSecret)

tweetData = streamClass.tweepy.Stream(auth, streamClass.collectTweets())
tweetData.filter(track=['apple', 'facebook', 'microsoft'], languages=['en'])


