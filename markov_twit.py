import tweepy

# saved their repo locally and make it take my string and gitignored it. sorry not sorry.
# just see http://www.pygaze.org/2016/03/how-to-code-twitter-bot/
# because i got lazy and must have not had enough data for markovify to return stuff.
from markovbot import MarkovBot

from twitter_credentials import API_KEY, API_SECRET_KEY
from twitter_credentials import ACCESS_TOKEN, ACCESS_TOKEN_SECRET

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
tweetbot.read('.\n'.join(trump_tweets_list + pope_tweets_list))

print(tweetbot.generate_text(25, seedword=['god', 'immigrants']))
