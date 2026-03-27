import telebot
from telebot import types

API_TOKEN ='8743125919:AAFnYbZ_R6lwKphWNZXVL60UJAt7AM9hGxo'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("📝 Homework")
    item2 = types.KeyboardButton("📢 Notice")
    item3 = types.KeyboardButton("💰 Fees")
    item4 = types.KeyboardButton("📞 Contact")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Gyanjyoti Smart School mein swagat hai! Button dabaiye:", reply_markup=markup)

# YAHAN SE REPLY KA JAADU SHURU HOTA HAI
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "📝 Homework":
        bot.reply_to(message, "Aaj ka Homework: Maths Ex-2.1 aur English Essay.")
    elif message.text == "📢 Notice":
        bot.reply_to(message, "Notice: Kal school ki chutti hai!")
    elif message.text == "💰 Fees":
        bot.reply_to(message, "Fees ki jankari ke liye apna Roll No. bhejein.")
    elif message.text == "📞 Contact":
        bot.reply_to(message, "Vashu Sir se sampark karein: +91 XXXXX-XXXXX")

bot.polling()
