        bot.send_message(message.chat.id, "❌ Maafi chahte hain, ye Roll Number galat hai.")

@bot.message_handler(func=lambda message: message.text == '📢 Notice')
def send_notice(message):
    bot.reply_to(message, "Notice: Kal school ki chutti hai!")

bot.polling()
