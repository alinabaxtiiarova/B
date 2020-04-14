import telebot
from telebot import types
bot = telebot.TeleBot('1141594126:AAGOHEhs7hFHMEUwJlYZOsjeDMf73JscbuY')

@bot.message_handler(commands=['trello'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти", url="https://trello.com"))
    bot.send_message(message.chat.id, "Не забудь заполнить", parse_mode='html', reply_markup=markup)
@bot.message_handler(commands=['yclients'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти", url="https://yclients.com"))
    bot.send_message(message.chat.id, "Расписание", parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    else :
        bot.send_message(message.from_user.id, "Доброй ночи!")

bot.polling(none_stop = True, interval = 0)
