import telebot
from telebot import types

# YAHAN APNA ASLI TOKEN REHNE DENA
API_TOKEN = '8743125919:AAFnYbZ_R6lwKphWNZXVL60UJAt7AM9hGxo'
bot = telebot.TeleBot(API_TOKEN)

# Bachon ka data
results_data = {
    "101": {"name": "Rahul Das", "class": "10", "marks": "85%", "status": "Pass"},
    "102": {"name": "Priya Borah", "class": "10", "marks": "92%", "status": "Pass"},
    "103": {"name": "Vashu Byas", "class": "10", "marks": "99%", "status": "Topper"}
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('📝 Homework')
    btn2 = types.KeyboardButton('📊 Results')
    btn3 = types.KeyboardButton('📢 Notice')
    btn4 = types.KeyboardButton('📞 Contact')
    markup.add(btn1, btn2, btn3, btn4)
    bot.reply_to(message, "Gyanjyoti Smart School mein swagat hai! Button dabaiye:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '📊 Results')
def ask_roll(message):
    msg = bot.send_message(message.chat.id, "Kripya apna Roll Number likhiye (Example: 101):")
    bot.register_next_step_handler(msg, process_result)

def process_result(message):
    roll = message.text
    if roll in results_data:
        student = results_data[roll]
        response = f"🎓 *Result Found!*\n\n👤 Name: {student['name']}\n📚 Class: {student['class']}\n📝 Marks: {student['marks']}\n✅ Status: {student['status']}"
        bot.send_message(message.chat.id, response, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "❌ Maafi chahte hain, ye Roll Number galat hai.")

@bot.message_handler(func=lambda message: message.text == '📢 Notice')
def send_notice(message):
    bot.reply_to(message, "Notice: Kal school ki chutti hai!")

bot.polling()
