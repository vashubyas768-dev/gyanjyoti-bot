import os
import telebot
from telebot import types
from flask import Flask
from threading import Thread

# 1. Flask Server (Bot ko 24/7 jagaye rakhne ke liye)
app = Flask('')
@app.route('/')
def home(): return "Gyanjyoti Bot is Awake!"

def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. Aapka Bot Setup
API_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

results_data = {
    "101": {"name": "Rahul Das", "class": "10"},
    "102": {"name": "Priya Borah", "class": "10"},
    "103": {"name": "Vashu Byas", "class": "10"}
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add('📝 Homework', '📊 Results', '📢 Notice', '📞 Contact')
    bot.reply_to(message, "Gyanjyoti Smart School Bot mein swagat hai!", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == '📊 Results')
def ask_roll(message):
    msg = bot.send_message(message.chat.id, "Kripya Roll Number bhejiye:")
    bot.register_next_step_handler(msg, process_result)

def process_result(message):
    roll = message.text
    if roll in results_data:
        res = results_data[roll]
        bot.send_message(message.chat.id, f"🎓 *Result Found*\n👤 Name: {res['name']}\n📚 Class: {res['class']}", parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "❌ Maaf kijiye, ye roll number nahi mila.")

import os
    
    # 1. Flask ko background mein chalu karein
    keep_alive() 
    
    # 2. Bot ko messages sunne ke liye chalu karein
    print("Bot is starting...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

