from telegram import *
from telegram.ext import *

token = "Ur TOKEN"


def hey_yo_function(update, context):
    update.message.reply_text(
        "Hey there!, you just successffully created a bot"
    )


def main():
    updater = Updater(token, use_context=True)
    dispatch = updater.dispatcher
    dispatch.add_handler(CommandHandler("welcome", hey_yo_function))
    updater.start_polling()
    updater.idle()


main()
