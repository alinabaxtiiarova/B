import telebot
from telebot import types
bot = telebot.TeleBot('1141594126:AAGOHEhs7hFHMEUwJlYZOsjeDMf73JscbuY')

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
button_hi1 = KeyboardButton('shshhsh')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)


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
        bot.send_message("Привет, чем я могу тебе помочь?")
    else :
        bot.send_message(message.from_user.id, "Доброй ночи!")
        

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Ghbdt', reply_markup=kb.greet_kb

bot.polling(none_stop = True, interval = 0)
