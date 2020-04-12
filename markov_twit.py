import os
import tweepy

# We need specifically this markovbot (not the pypi one):
# https://github.com/esdalmaijer/markovbot
# So I just cloned it locally for now.
from markovbot import MarkovBot

from twitter_credentials import API_KEY, API_SECRET_KEY
from twitter_credentials import ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Choose your own! It helps to pick from both Trumpish words and papal-sounding
# words. For example, you could seed with ['america', 'god']
SEEDWORDS = ['crisis']

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Connect via credentials!
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

trump_cursor = tweepy.Cursor(
    api.user_timeline, screen_name='POTUS', count=500, tweet_mode='extended')
trump_tweets_list = list(filter(
    None, [getattr(tweet, 'full_text', None) for tweet in trump_cursor.iterator.next()]
))
pope_cursor = tweepy.Cursor(
    api.user_timeline, screen_name='Pontifex', count=500, tweet_mode='extended')
pope_tweets_list = list(filter(
    None, [getattr(tweet, 'full_text', None) for tweet in pope_cursor.iterator.next()]
))
tweetbot = MarkovBot()

try:
    with open('tweets.txt', 'w') as tweetfile:
        tweetfile.write('.\n'.join(trump_tweets_list + pope_tweets_list))
except UnicodeEncodeError:
    print('Unicode sadness occurred when reading tweets file. '
          'I told you to use Python3+ >:-(')
else:
    tweetbot.read('tweets.txt')
    print(tweetbot.generate_text(25, seedword=SEEDWORDS))
finally:
    os.remove('tweets.txt')
