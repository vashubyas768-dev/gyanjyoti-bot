import os
import telebot
from telebot import types
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Gyanjyoti Bot is Running"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Aapka Sahi Token
API_TOKEN = "8743125919:AAFnYbZ_R6lwKphWNZXVL60UJAt7AM9hGxo"
bot = telebot.TeleBot(API_TOKEN)

# Student Data
students_data = {
    "101": {"name": "Rahul Das", "class": "10th", "status": "Pass"},
    "102": {"name": "Priya Borah", "class": "10th", "status": "Pass"},
    "103": {"name": "Vashu Byas", "class": "10th", "status": "Topper"}
}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("📝 Homework")
    btn2 = types.KeyboardButton("📊 Results")
    btn3 = types.KeyboardButton("📢 Notice")
    btn4 = types.KeyboardButton("📞 Contact")
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.send_message(message.chat.id, "Namaste! Gyanjyoti AI Tutor mein aapka swagat hai. Roll Number bhejiye ya button chuniye.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text

    if text == "📊 Results":
        bot.reply_to(message, "Apna Roll Number (e.g., 101) likh kar bhejiye.")
    
    elif text == "📞 Contact":
        bot.reply_to(message, "Aap humein support@gyanjyoti.com par email kar sakte hain.")
    
    elif text == "📝 Homework":
        bot.reply_to(message, "Aaj ka homework: Math Exercise 2.1 solve karein.")

    elif text == "📢 Notice":
        bot.reply_to(message, "Kal school ki chutti hai.")

    # Agar user Roll Number likhta hai
    elif text in students_data:
        student = students_data[text]
        response = f"🎓 Name: {student['name']}\n📚 Class: {student['class']}\n✅ Status: {student['status']}"
        bot.reply_to(message, response)
    
    else:
        bot.reply_to(message, "Maaf kijiye, ye sahi Roll Number nahi hai. Kripya 101, 102 ya 103 try karein.")

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
