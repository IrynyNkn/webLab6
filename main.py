import telebot

BOT_TOKEN = '6860812526:AAEtqhxwHDA6muC1Lyt2NP_rBZRIF2la79E'

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()


# if __name__ == '__main__':
#     print('Hi')