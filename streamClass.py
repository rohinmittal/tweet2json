import tweepy, json, datetime, urllib
from tweepy.api import API

_consumerToken = "enter_your_consumer_token"
_consumerSecret = "enter your consumer secret"
_accessToken = "enter your access token"
_accessSecret = "enter your access secret"

class collectTweets(tweepy.StreamListener):
    def __init__(self, api=None):
	self.api = api or API()
	self.dataStored = ""
	self.start = 0
	self.end = 1000

	def on_error(self, status_code):
	    if status_code == 420:
		    return False

	    def on_data(self, data):
		status = json.loads(data)

		if 'retweeted_status' not in status:
			print "{"

			print "\"id\" : " + "\"" + str(status['id']) + "\","
			dt = datetime.datetime.strptime(str(status['created_at']), '%a %b %d %H:%M:%S +0000 %Y').strftime('%Y-%m-%dT%H:%M:%SZ')
			print "\"created_at\" : " + "\"" + dt + "\","

			if 'lang' in status:
				print "\"lang\" : " + "\"" + str(status['lang']) + "\","

			text_string = str(status['text'].encode("utf-8"))
			text_string = text_string.replace("\"", " ")
			if self.dataStored.find(text_string) != -1: 
				return False
			else:
				self.dataStored = self.dataStored + text_string 
	
			if self.start == self.end:
				return False
			else:
				self.start += 1

			if status['lang'] == 'en':
				print "\"text_en\" : " + "\"" + text_string + "\","
				print "\"text_ru\" : \"\","
				print "\"text_de\" : \"\","
			elif status['lang'] == "ru":
				print "\"text_en\" : \"\","
				print "\"text_ru\" : " + "\"" + text_string + "\","
				print "\"text_de\" : \"\","
			elif status['lang'] == 'de':
				print "\"text_en\" : \"\","
				print "\"text_ru\" : \"\","
				print "\"text_de\" : " + "\"" + text_string + "\","

			hTags = []
			for hashTags in status['entities']['hashtags']:
				hTags.append("\"" + hashTags['text'].encode("utf-8") + "\"")
			print "\"tweet_hashtags\" : [" + ', '.join(hTags) + "],"

			eURLs = []
			for url in status['entities']['urls']:
				eURLs.append("\"" + url['expanded_url'].encode("utf-8") + "\"")
			print "\"tweet_urls\" : [" + ', '.join(eURLs) + "]"

			print "},"
