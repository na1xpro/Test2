import telebot
import config
import pyowm

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/Botpogoda.png','rb')
    bot.send_sticker(message.chat.id, sti)


    bot.send_message(message.chat.id,
                     "Добро пожаловать,{0.first_name}!\nЯ - <b>{1.first_name}</b>, бот который предоставляет температуру в данном городе. ".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

    city = bot.send_message(message.chat.id,
                    "Напиши в чат,город в каком ты хочешь узнать о погоде?"

    #Код самой програмы погоды








@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Киев":
            bot.send_message(message.chat.id, ".")
        elif message.text == "?":
            bot.send_message(message.chat.id, "т)")

    # Начало


bot.polling(none_stop=True)
