How to use this yourself?!
--------------------------
- Set yourself up for the Twitter API! [Here](http://www.pygaze.org/2016/03/how-to-code-twitter-bot/) is an example with instructions for creating an app and obtaining keys/access tokens.
- Make a twitter_credentials.py (gitignored because security!) It needs to look like this:
```
API_KEY = <your_api_key>
API_SECRET_KEY = <your_secret_key>
ACCESS_TOKEN = <your_access_token>
ACCESS_TOKEN_SECRET = <your_access_token_secret>
```
- The [specific MarkovBot we use](https://github.com/esdalmaijer/markovbot) is not the pypi one, so you can install it locally right in this directory. Sue me.
- Choose your seed words, and update the list in `markov_twit.py` accordingly.
- `python markov_twit.py` . This should be Python 3+, of course, unless you wanna go to Unicode hell.
