import telebot

#
bot = telebot.TeleBot('7840973047:AAFGM-N0q7xYBmu7UP9qct9DKdDwtUeHtjA')

@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"Ваш chat_id: {chat_id}")

bot.polling()
