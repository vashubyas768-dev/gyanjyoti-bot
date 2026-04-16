import telebot

# Apna Naya Token Quotes ke andar dhyan se check karke daliye
API_TOKEN ='8676020356:AAFe_kbP-brrprJpFRviRkdtnhAOSbghkyc' 
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaskar Vashu Sir! Sivasagar AI Bot ab puri tarah LIVE hai! 🚀")

print("Bot is starting...")
bot.infinity_polling()
