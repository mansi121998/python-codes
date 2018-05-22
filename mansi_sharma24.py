import tweepy
 
# personal details
consumer_key ="VbWZgzIt49an8U1ASmGvBZBN3"
consumer_secret ="fWtox7CRiPMFtiyOgAXYNGpTslImZaedE9fP7iYhgO0Vf0ahMj"
access_token ="771617182690086913-93nqBNjamtUnGB51LIvDLJBRE9ohvZx"
access_token_secret ="szHwhzlifubfeUHEK7pdkJJAMwj95sRRh0hVU0dacEROZ"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
