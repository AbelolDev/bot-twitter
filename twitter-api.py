# AbelolDev project

# Twitter bot:
# a Twitter bot that responds to mentions 
# retweet certain hashtags
# or post tweets


import tweepy
import time

# credentials
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'


# authentication with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Functions
def get_api_keys():
    print("Please provide Twitter API keys: ")
    consumer_key = input("Consumer Key: ")
    consumer_secret = input("Consumer Secret: ")
    access_token = input("Access Token: ")
    access_token_secret = input("Access Token Secret: ")

# Return a dictionary with the keys
    keys = {
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret,
        'access_token': access_token,
        'access_token_secret': access_token_secret
    }

    return keys

def reply_mentions():
    print("Looking for mentions...")
    mention = api.mentions_timeline()

    for mencion in reversed(mention):
        if mencion.in_reply_to_status_id is None:
            print(f"Replying to @{mention.user.screen_name}")
            api.update_status(
                status=f"Hi @{mencion.user.screen_name}! I'm a Twitter bot created by AbelDev with Python, how can I help you?",
                in_reply_to_status_id=mencion.id
            )
            print("Answered!")
            time.sleep(20)  # Avoid the limit of requests

def get_user_data(screen_name):
    try:
        api.get_user(screen_name=screen_name)
    except Exception as e:
        print(f"Error: {e}")

def publish_tweet(message):
    tweet_text = f"{message}"
    api.update_status(status=tweet_text)
    print("Send")
    time.sleep(20) # Avoid request limit.

def switch_case(option):
    if option == "1":
        print("You selected option 1.")
        print("")
        reply_mentions()
    elif option == "2":
        print("You selected option 2.")
        print("")
        screen_name = str(input("Enter the user name: "))
        get_user_data(screen_name)
    elif option == "3":
        print("You selected option 3.")
        print("")
        message  = str(input("Enter the message to send: "))
        publish_tweet(message)
    elif option == "4":
        print("You selected option 4.")
        print("")
        get_api_keys()
    else:
        print("Invalid option.")

# Run the application
print("")
print("Developed by AbelDev")
print("")
while True:
    print("Select option: ")
    print("1-) Reply to mentions")
    print("2-) Get public data from a user")
    print("3-) Post a tweet (text only)")
    print("4-) Configure API keys")
    print("5-) Close the app")
    option = str(input(">>> "))

    if option != "5":
        switch_case(option)
    else:
        print("Exiting the app")
        break