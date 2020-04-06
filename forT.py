import telebot
bot = telebot.TeleBot('1141594126:AAGOHEhs7hFHMEUwJlYZOsjeDMf73JscbuY')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    bot.send_message(message.chat.id, message.text)
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    else :
        bot.send_message(message.from_user.id, "Доброй ночи!")

bot.polling(none_stop = True, interval = 0)
