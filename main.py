import telebot
import config
import database
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def startCommand(message):
    database.startCommand(message.chat.id)
    bot.send_message(message.chat.id, database.sendCurrentInput(message.chat.id), reply_markup=database.sendCurrentMarkup(message.chat.id))


@bot.message_handler(content_types=["text"])
def textCommand(message):
    text = database.processMessage(message.chat.id, message.text)
    if text: bot.send_message(message.chat.id, text)
    bot.send_message(message.chat.id, database.sendCurrentInput(message.chat.id), reply_markup = database.sendCurrentMarkup(message.chat.id))




bot.polling(none_stop=True)