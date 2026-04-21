import telebot
import os
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def hello():
    return "Gyanjyoti Bot is Running!"

# Sahi Token jo BotFather ne diya tha
API_TOKEN = '8676020356:AAFz-kraG7h2cltotemx63KVD8RCFPNltO8'
                        
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaskar Vashu Sir! Gyanjyoti AI Tutor active hai.")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
if "Homework" in message.text:
        bot.reply_to(message, "📚 Aaj ka homework: Math Exercise 2.1 solve karein.") elif "Results" in message.text:
        bot.reply_to(message, "📊 Apna Roll Number likh kar bhejiye.")
elif "Notice" in message.text:
        bot.reply_to(message, "📢 Kal school mein chutti hai.")
elif "Contact" in message.text:
        bot.reply_to(message, "📞 Sivasagar Office: 9876543210")
else:
        bot.reply_to(message, "Main aapki kya madad kar sakta hoon?")

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
