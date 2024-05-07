import telebot
import gunicorn 
from test import server 
import threading 
from time import sleep 
bot = telebot.TeleBot('7156177907:AAHaTVyqCyfLap86H3Gcfv8yei6FkrrfRck')
a = 0
@bot.message_handler(commands=['start'])
def ss(message):
	bot.reply_to(message ,'welcom')
def yy():
	global a
	while True:
		a +=1
		bot.send_message(1558155028 ,f'تم التحديث :{a}')
		sleep(60)
threading.Thread(target=yy).start()
server()
bot.infinity_polling()
