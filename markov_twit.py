import tweepy

from twitter_credentials import API_KEY, API_SECRET_KEY
from twitter_credentials import ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Connect via credentials!
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

for status in tweepy.Cursor(api.home_timeline).items(200):
	print(status._json)
