import telebot

from settings import Config

bot = telebot.TeleBot(Config.TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")


bot.infinity_polling()