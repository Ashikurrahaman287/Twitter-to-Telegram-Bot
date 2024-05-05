import tweepy
from telegram.ext import Updater, CommandHandler
from telegram import ParseMode

# Twitter API credentials
consumer_key = 'spudblocks.com'
consumer_secret = 'spudblocks.com'
access_token = 'spudblocks.com'
access_token_secret = 'spudblocks.com'

# Telegram bot token
telegram_token = 'spudblocks.com'

# Initialize Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Initialize Telegram bot
updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a Twitter bot! Send me /tweet to get the latest tweet.")

def tweet(update, context):
    # Retrieve the latest tweet
    latest_tweet = api.user_timeline(screen_name='@spudblocks', count=1)[0]

    # Send the tweet to the Telegram group
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{latest_tweet.text}")

# Register handlers
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

tweet_handler = CommandHandler('tweet', tweet)
dispatcher.add_handler(tweet_handler)

# Start the bot
updater.start_polling()
updater.idle()
