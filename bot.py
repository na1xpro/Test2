import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.jfif','rb')
    bot.send_sticker(message.chat.id, sti)

    # Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("В чем сила?")
    item2 = types.KeyboardButton("Почему GTA 5 бесплатная?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать,{0.first_name}!\nЯ - <b>{1.first_name}</b>, бот пиздабол. ".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])


def lalala(message):
    if message.chat.type == 'private':
        if message.text == "В чем сила?!":
            bot.send_message(message.chat.id, "В душе не ебу!,я же бот.")
        elif message.text == "Почему GTA 5 бесплатная?":
            bot.send_message(message.chat.id, "Я ебу,хули они раздают)")

    # Начало


bot.polling(none_stop=True)
