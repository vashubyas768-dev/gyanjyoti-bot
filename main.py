import telebot
from telebot import types

API_TOKEN ='8676020356:AAGSYUgI6WXY_QSWNd3idu2hd1Rv6hH9uIs' 
bot = telebot.TeleBot(API_TOKEN)

students_data = {
    "101": {"name": "Rahul Borah", "result": "Pass (85%)", "school": "Sibsagar Govt. H.S. School"},
    "102": {"name": "Priyanka Saikia", "result": "Pass (92%)", "school": "Nazira Model School"},
    "103": {"name": "Aman Ahmed", "result": "Pass (78%)", "school": "Gyanjyoti Smart School"}
}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('📊 Results / ফলাফল')
    btn2 = types.KeyboardButton('📞 Contact / যোগাযোগ')
    markup.add(btn1, btn2)
    welcome_text = "नमस्कार! Gyanjyoti AI Tutor লৈ স্বাগতম।\nNamaste! Gyanjyoti AI Tutor mein aapka swagat hai."
    bot.reply_to(message, welcome_text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '📊 Results / ফলাফল')
def ask_roll(message):
    msg = bot.send_message(message.chat.id, "Please enter Roll Number / অনুগ্ৰহ কৰি ৰোল নম্বৰ লিখক:")
    bot.register_next_step_handler(msg, process_roll)

def process_roll(message):
    roll = message.text
    if roll in students_data:
        s = students_data[roll]
        res = f"✅ *Result Found!*\n\n👤 Name: {s['name']}\n🏫 School: {s['school']}\n📝 Status: {s['result']}"
        bot.send_message(message.chat.id, res, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "❌ Roll Number not found / ৰোল নম্বৰ পোৱা নগ'ল।")

bot.infinity_polling()
