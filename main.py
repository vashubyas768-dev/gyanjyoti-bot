import telebot
import os
from flask import Flask

# 1. Flask setup (Render ko dhoka dene ke liye)
app = Flask(__name__)

@app.route('/')
def hello():
    return "Bot is running!"

# 2. Bot setup
API_TOKEN ='8676020356:AAGSYUgI6WXY_QSWNd3idu2hd1Rv6hH9uIs'
                ' # Naya Token yahan check karke daliye
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaskar Vashu Sir! Port problem solved. Bot is LIVE! 🚀")

# 3. Dono ko saath chalane ka tarika
if __name__ == "__main__":
    # Bot ko background mein shuru karein
    import threading
    threading.Thread(target=bot.infinity_polling).start()
    
    # Port bind karna (Render ki demand poori karna)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
