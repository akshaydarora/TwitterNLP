# Importing Dependencies #Twitter and TextBlob
import tweepy
from textblob import TextBlob

# Authenticate with Key and Token Method

# Consumer KEY
consumer_key= 'lr9r1zttD7bCz99nxhvytYP0v'
consumer_secret= 'VbkQoxtdNIBrg0OXe56aIsl3k5Ziy8FIuUcbtyY5UW32LNxqzA'

# Consumer TOKEN
access_token='842577644604592129-NmgOGVYLhXjQq55DbvKfsPqqftnnXEf'
access_token_secret='U7CjfGyBOWIR9ZUmPPR3saDbI0O2FXZbI5OLxYc4R4AEQ'

# Create an Authenication Variable

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# Generate a twitter API
api = tweepy.API(auth)

# Find Tweets with the Given Name
public_tweets = api.search('Hilary Clinton')

# Search For  all tweets with this name

for tweet in public_tweets:
    print(tweet.text)
    
# Perform Sentiment Analysis on Tweets and see its polarity('Positive' or 'Negative')
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
