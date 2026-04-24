import telebot
from flask import Flask, request
import os

# 1. Setup
API_TOKEN = '8676020356:AAFz-kraG7h2cltotemx63KVD8RCFPNltO8'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# 2. Keyboards (Buttons)
def main_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('📝 Homework')
    btn2 = telebot.types.KeyboardButton('📊 Results')
    btn3 = telebot.types.KeyboardButton('👨‍🏫 Staff Info')
    btn4 = telebot.types.KeyboardButton('📞 Contact')
    markup.add(btn1, btn2, btn3, btn4)
    return markup

# 3. Handlers
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, 
        "✅ Gyanjyoti AI Tutor Active Hai!\n\nNiche diye gaye buttons se jankari lein.", 
        reply_markup=main_keyboard()
    )

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == '👨‍🏫 Staff Info':
        # Aapki di hui updated list yahan hai:
        staff_details = (
            "🏫 **Gyanjyoti School Staff Details:**\n\n"
            "👤 **Principal:** Devajani Saikia Gogoi\n"
            "🎓 **Incharge:** Dimpi Chetia\n"
            "📖 **Teachers:**\n"
            "• Momi Neog\n"
            "• Himasree Gogoi\n\n"
            "📍 **Location:** Nazira, Sivasagar, Assam"
        )
        bot.reply_to(message, staff_details)
    
    elif message.text == '📝 Homework':
        bot.reply_to(message, "📚 Homework Section: Portal update ho gaya hai.")
        
    elif message.text == '📊 Results':
        bot.reply_to(message, "📊 Results: Digital marksheets jald hi upload hongi.")
        
    elif message.text == '📞 Contact':
        bot.reply_to(message, "📞 Contact: Aap school office mein sampark kar sakte hain.")

# 4. Webhook Receiver
@app.route('/8676020356:AAfz-kraG7h2c8_S6yXp3G6L6P78J4_U5s8', methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    return "<h1>Gyanjyoti Bot: Staff List Updated! ✅</h1>", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
