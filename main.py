import os
import telebot
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Gyanjyoti Bot is Running"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

API_TOKEN ="8743125919:AAFnYbZ_R6lwKphWNZXVL60UJAt7AM9hGxo"                       "
bot = telebot.TeleBot(API_TOKEN)

results_data = {
    "101": {"name": "Rahul Das", "class": "10"},
    "102": {"name": "Priya Borah", "class": "10"},
    "103": {"name": "Vashu Byas", "class": "10"}
}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Namaste! Roll Number bhejiye.")

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    roll = message.text.strip()
    if roll in results_data:
        s = results_data[roll]
        bot.reply_to(
            message,
            f"Result Mil Gaya\nNaam: {s['name']}\nClass: {s['class']}"
        )
    else:
        bot.reply_to(message, "Roll Number nahi mila")

if __name__ == "__main__":
    keep_alive()
    print("Bot Started")
    bot.infinity_polling()
