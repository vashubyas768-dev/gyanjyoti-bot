import telebot
from flask import Flask, request
import os
import requests

# 1. Setup - Bilkul sahi Token
API_TOKEN = '8653944194:AAFl578Ww7LQkN5_YH2GGLUsb3awAR0ol18'

                            
RENDER_URL = 'https://gyanjyoti-smart-bot-final.onrender.com'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# 2. AUTO-WEBHOOK SETTER (Yeh link ki zaroorat khatam kar dega)
def set_webhook():
    webhook_url = f"{RENDER_URL}/{API_TOKEN}"
    url = f"https://api.telegram.org/bot{API_TOKEN}/setWebhook?url={webhook_url}"
    response = requests.get(url)
    return response.json()

# 3. Staff List Handler
@bot.message_handler(func=lambda message: message.text == '👨‍🏫 Staff Info')
def staff_info(message):
    details = (
        "🏫 **Gyanjyoti School Staff:**\n\n"
        "👤 **Principal:** Devajani Saikia Gogoi\n"
        "🎓 **Incharge:** Dimpi Chetia\n"
        "📖 **Teachers:** Momi Neog, Himasree Gogoi\n\n"
        "📍 Nazira, Sivasagar"
    )
    bot.reply_to(message, details)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('📝 Homework', '📊 Results', '👨‍🏫 Staff Info', '📞 Contact')
    bot.send_message(message.chat.id, "✅ Gyanjyoti AI Tutor Update Ho Gaya Hai!", reply_markup=markup)

# 4. Webhook Receiver
@app.route(f'/{API_TOKEN}', methods=['POST'])
def receive_update():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def home():
    # Jab bhi aap ye page kholenge, webhook khud set ho jayega!
    status = set_webhook()
    return f"<h1>Gyanjyoti Bot Status: {status}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
