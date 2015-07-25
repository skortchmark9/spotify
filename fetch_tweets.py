import argparse
import oauth2 as oauth
import urllib2 as urllib
import json
import sys
import csv

# See Assignment 1 instructions for how to get these credentials
access_token_key = "3071366253-WJMCcY10iQttEkp5k7NschIyDkutZMnMfkdCC8R"
access_token_secret = "hAJgfu08sdxnuqwr64mtg1eAonOjwFZkXnJSuidi1ddLI"

consumer_key = "bQCyC9lvLQTYd9pZ84MqFE2W9"
consumer_secret = "eQi2uHNg3dm9aoQUzmS6MI8qzKxp93EkNVE71wmpZ93ZhgtQsw"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
    req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

    req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

    headers = req.to_header()

    if http_method == "POST":
        encoded_post_data = req.to_postdata()
    else:
        encoded_post_data = None
        url = req.to_url()

    opener = urllib.OpenerDirector()
    opener.add_handler(http_handler)
    opener.add_handler(https_handler)

    response = opener.open(url, encoded_post_data)

    return response

def fetch_samples():
    url = "https://stream.twitter.com/1.1/statuses/sample.json?language=en"
    parameters = []
    response = twitterreq(url, "GET", parameters)
    for line in response:
        print line.strip()

def fetch_by_terms(term):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    parameters = [("q", term), ("count", 10)]
    response = json.loads(twitterreq(url, "GET", parameters).read())
    for tweet in response['statuses']:
	    print(json.dumps(tweet))

def fetch_by_user_names(user_name_file):
    sn_file = open(user_name_file)
    writer = csv.writer(sys.stdout)
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    writer.writerow(("user_name", "tweet"))

    for user in sn_file:
        user = user.strip()
        parameters = [('screen_name', user), ('count', 100)]
        response = json.loads(twitterreq(url, "GET", parameters).read())
        for tweet in response:
            writer.writerow((user, tweet['text'].encode('utf-8')))




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', required=True, help='Enter the command')
    parser.add_argument('-term', help='Enter the search term')
    parser.add_argument('-file', help='Enter the user name file')
    opts = parser.parse_args()
    if opts.c == "fetch_samples":
        fetch_samples()
    elif opts.c == "fetch_by_terms":
        term = opts.term
        fetch_by_terms(term)
    elif opts.c == "fetch_by_user_names":
        user_name_file = opts.file
        fetch_by_user_names(user_name_file)
    else:
        raise Exception("Unrecognized command")
