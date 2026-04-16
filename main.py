import telebot
from telebot import types

# AAPKA NAYA TOKEN
API_TOKEN = '8676020356:AAGSYUgI6WXY_QSWNd3idu2hd1Rv6hH9uIs'
bot = telebot.TeleBot(API_TOKEN)

students_data = {
    "101": {"name": "Rahul Borah", "result": "Pass (85%)", "school": "Sibsagar Govt. H.S. School"},
    "102": {"name": "Priyanka Saikia", "result": "Pass (92%)", "school": "Nazira Model School"}
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('📊 Results / ফলাফল')
    markup.add(btn1)
    bot.reply_to(message, "नमस्कार! Gyanjyoti AI Tutor লৈ স্বাগতম।", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '📊 Results / ফলাফল')
def ask_roll(message):
    msg = bot.send_message(message.chat.id, "Roll Number likhiye / ৰোল নম্বৰ লিখক:")
    bot.register_next_step_handler(msg, process_roll)

def process_roll(message):
    roll = message.text
    if roll in students_data:
        s = students_data[roll]
        res = f"
