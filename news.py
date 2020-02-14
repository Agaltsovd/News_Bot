#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
#
# THIS EXAMPLE HAS BEEN UPDATED TO WORK WITH THE BETA VERSION 12 OF PYTHON-TELEGRAM-BOT.
# If you're still using version 11.1.0, please see the examples at
# https://github.com/python-telegram-bot/python-telegram-bot/tree/v11.1.0/examples

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import requests
import json

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Привет, Я бот, меня сделал Данияр, потому что ему было скучно \n')
    update.message.reply_text('Я помогу вам найти новости, интересующие вас \n')
    update.message.reply_text('Просто введите код страны, которая интересует вас и я покажу вам главные новости')



def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def news(update, context):
    mes = update.message.text

    url = ('https://newsapi.org/v2/top-headlines?'
           'country='+mes+'&'
           'apiKey=a6d36b9aa5ac41bfbb3f83f57d39a00e')
    response = requests.get(url)
    y = response.json()

    update.message.reply_text(" - "+y["articles"][0]['description']+"\n")
    update.message.reply_html(y["articles"][0]['url'])
    update.message.reply_html(y["articles"][0]['urlToImage'])
    update.message.reply_text(" - " + y["articles"][1]['description'] + "\n")
    update.message.reply_html(y["articles"][1]['url'])
    update.message.reply_html(y["articles"][1]['urlToImage'])
    update.message.reply_text(" - " + y["articles"][2]['description'] + "\n")
    update.message.reply_html(y["articles"][2]['url'])
    update.message.reply_html(y["articles"][2]['urlToImage'])
    update.message.reply_text("With love from Daniyar")



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("927484737:AAEfq27m4jH1QpipHQO30betVhpQwucpw90", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, news))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
