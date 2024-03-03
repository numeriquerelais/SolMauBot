import telebot
from typing import Final

TELEGRAM_API_KEY : Final[str] = ''

bot = telebot.TeleBot(TELEGRAM_API_KEY)
bot_name = "l'Aimo-droïde"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f'Bonjour, je suis {bot_name}, pour vous servir')
	
@bot.message_handler(func=lambda m: True)
def echo(message):
	bot.reply_to(message, 'Bien reçu.')
	
@bot.message_handler(commands=['blague'])
def send_welcome(message):
	bot.reply_to(message, f"C'est l'histoire d'un aveugle qui rentre dans un bar. Et dans une table, et dans une chaise, et dans un mur, etc")
	
bot.infinity_polling()