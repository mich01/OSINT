import tweepy

# Replace with your own API key, API secret key, access token, and access token secret
consumer_key = 'ant400sEsPLvc0zAUkCffsf98'
consumer_secret = 'IUQxEjtYmXg8jwyI62uWWXoPbVAchoeEqT12onzOrdK20XtaOn'
access_token = '65900718-3JiVuwZ5VI7jXXzLOgRPd8PzxJ7wtrDcubcExvBil'
access_token_secret = 'beaF1iSwT9vwhgXdb6jJ9T1SytgLBpmjARsb4h2zgyF9P'


auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

# If the authentication was successful, this should print the
# screen name / username of the account
print(api.verify_credentials().screen_name)

api.update_status("Why does Tweeter lock out its apis?")