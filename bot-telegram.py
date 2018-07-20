import telebot
from axnio import *

bot = telebot.TeleBot("608340566:AAGFCLgvT5yZWmeaZu20TGN5X71cv7oCYS0")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, conversacion(message))

print("Escuchando...")
bot.polling()
