import telebot
from telebot import types

# Yahan apna wahi purana API TOKEN daliye
API_TOKEN ='8743125919:AAFnYbZ_R6lwKphWNZXVL60UJAt7AM9hGxo'
bot = telebot.TeleBot(API_TOKEN)

# --- Real Data (Sivasagar School Sample) ---
# Isse hum baad mein alag file mein bhi rakh sakte hain
students_data = {
    "101": {"name": "Rahul Borah", "result": "Pass (85%)", "school": "Sibsagar Govt. H.S. School"},
    "102": {"name": "Priyanka Saikia", "result": "Pass (92%)", "school": "Nazira Model School"},
    "103": {"name": "Aman Ahmed", "result": "Pass (78%)", "school": "Amguri High School"}
}

# --- Welcome Message (Bilingual) ---
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('📚 Homework / ঘৰৰ কাম')
    itembtn2 = types.KeyboardButton('📊 Results / ফলাফল')
    itembtn3 = types.KeyboardButton('📢 Notice / জাননী')
    itembtn4 = types.KeyboardButton('📞 Contact / যোগাযোগ')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    
    welcome_text = (
        "नमस्कार! Gyanjyoti AI Tutor লৈ স্বাগতম।\n\n"
        "Namaste! Gyanjyoti AI Tutor mein aapka swagat hai.\n"
        "Please choose an option / অনুগ্ৰহ কৰি এটা বিকল্প বাছনি কৰক।"
    )
    bot.reply_to(message, welcome_text, reply_markup=markup)

# --- Result Logic ---
@bot.message_handler(func=lambda message: message.text in ['📊 Results / ফলাফল'])
def ask_roll(message):
    msg = bot.send_message(message.chat.id, "আপোনাৰ ৰোল নম্বৰ লিখক (e.g., 101):\nApna Roll Number likhiye:")
    bot.register_next_step_handler(msg, process_roll)

def process_roll(message):
    roll = message.text
    if roll in students_data:
        student = students_data[roll]
        res = (
            f"✅ *Result Found!*\n\n"
            f"👤 Name: {student['name']}\n"
            f"🏫 School: {student['school']}\n"
            f"📝 Status: {student['result']}\n\n"
            f"Powered by Vashu AI Labs, Sivasagar"
        )
        bot.send_message(message.chat.id, res, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "❌ Roll Number not found. / ৰোল নম্বৰ পোৱা নগ'ল।")

# Bot ko zinda rakhne ke liye (Render par kaam karega)
bot.infinity_polling()
