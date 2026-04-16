import telebot
import os
from flask import Flask
import threading

# 1. Flask setup (Render port problem solve karne ke liye)
app = Flask(__name__)

@app.route('/')
def hello():
    return "Bot is running!"

# 2. Bot setup
# Yahan apna Naya Token Quotes ke andar bilkul sahi se likhiye
API_TOKEN ='8676020356:AAGSYUgI6WXY_QSWNd3idu2hd1Rv6hH9uIs'
               ' 
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaskar Vashu Sir! Sivasagar AI Bot ab LIVE hai! 🚀")

def run_bot():
    bot.infinity_polling()

# 3. Execution
if __name__ == "__main__":
    # Bot ko doosre raste (thread) par shuru karein
    threading.Thread(target=run_bot).start()
    
    # Render ke liye port chalu karna
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
