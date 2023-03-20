from datetime import datetime
import psycopg2
conn = psycopg2.connect(dbname='komandor', user='postgres', password='', host='194.67.65.146')
cursor = conn.cursor()
import telebot
from telebot import types

bot = telebot.TeleBot('6069432036:AAG4sD4wgScTQXZ9quIk_Lq_44AKCEDOQe8')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Внести данные о продаже')
    markup.add(btn1)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Внести данные о продаже':
        bot.send_message(message.from_user.id, 'Введите сумму продажи')
    if message.text.isdigit() is True:
        dv = (datetime.now(), int(message.text))
        print(dv)
        cursor.execute("INSERT INTO bot (date, value) VALUES (%s, %s)", dv)
        conn.commit()
        print('Данные добавлены')
        bot.send_message(message.from_user.id, 'Данные добавлены')

bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть
