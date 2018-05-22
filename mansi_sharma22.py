import  time
import urllib2
import json
import oauth2


url1 = "https://api.twitter.com/1.1/search/tweets.json"  # FIXED AUTHENCATION PARAMETERS

params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }

consumer = oauth2.Consumer(key="TBUe0iD3p2tLJWOWk5E8bbURc", 
                           secret="tLYGKX6hqGNSAAnLFU9crk2f6uMrooWRCDfaTcDihLUL5uA2mp")

token = oauth2.Token(key="771617182690086913-93nqBNjamtUnGB51LIvDLJBRE9ohvZx",
                     secret="szHwhzlifubfeUHEK7pdkJJAMwj95sRRh0hVU0dacEROZ")

params["oauth_consumer_key"] = consumer.key   # VARIABLE AUTHENCATION PARAMETERS

params["oauth_token"] = token.key

params["q"]="jaipur"

req = oauth2.Request(method="GET", url=url1, parameters=params)
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token)
url = req.to_url()
response = urllib2.Request(url)
data = json.load(urllib2.urlopen(response))

filename = params["q"]      
f = open(filename + "_File.txt", "w")  
json.dump(data["statuses"], f)
f.close()
6+12*3


