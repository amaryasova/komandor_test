import psycopg2
conn = psycopg2.connect(dbname='komandor', user='postgres', password='xxx', host='194.67.65.146')
cursor = conn.cursor()
import telebot
from telebot import types

bot = telebot.TeleBot('6069432036:AAG4sD4wgScTQXZ9quIk_Lq_44AKCEDOQe8')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Внести данные о продаже")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Данные внесены", reply_markup=markup)

@bot.message_handler(content_types=['bigint'])
def get_text_messages(message):

    if message.text.type is bigint:
        cursor.execute("INSERT INTO bot (date, value) VALUES (date.today(), message.text)")
		conn.commit()  
		print("Данные добавлены")
 
cursor.close()
conn.close()

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
