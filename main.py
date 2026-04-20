import telebot
import os
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def hello():
    return "Gyanjyoti Bot is Running!"

# Naya Token yahan sahi se daliye
API_TOKEN='8676020356:AAFz-kraG7h2cltotemx63KVD8RCFPNltO8'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaskar Vashu Sir! Gyanjyoti AI Tutor mein aapka swagat hai. Main ab live hoon!")

# Buttons ka jawab dene ke liye ye hissa zaroori hai
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if "Homework" in message.text:
        bot.reply_to(message, "📚 Aaj ka homework: Math Exercise 2.1 solve karein.")
    elif "Results" in message.text:
        bot.reply_to(message, "📊 Apna Roll Number likh kar bhejiye.")
    elif "Notice" in message.text:
        bot.reply_to(message, "📢 Kal school mein 10 baje meeting hai.")
    elif "Contact" in message.text:
        bot.reply_to(message, "📞 Contact: +91-XXXX-XXXXXX (Sivasagar Office)")
    else:
        bot.reply_to(message, "Main aapki kya madad kar sakta hoon?")

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
