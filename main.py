import telebot
import os
from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bot is running!"

# Is line mein apna naya token quotes ke andar bilkul sahi se likhiye
API_TOKEN ='8676020356:AAGSYUgI6WXY_QSWNd3idu2hd1Rv6hH9uIs'
             
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaskar Vashu Sir! Sivasagar AI Bot ab Render par LIVE hai! 🚀")

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # Bot ko background mein chalane ke liye
    threading.Thread(target=run_bot).start()
    # Render ke liye port setup
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
