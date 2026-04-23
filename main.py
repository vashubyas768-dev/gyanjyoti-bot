import telebot
from flask import Flask, request
import os
import requests # Ek extra library connection check ke liye

# 1. Bot Setup
API_TOKEN = '8676020356:AAFz-kraG7h2cltotemx63KVD8RCFPNltO8'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# 2. Handlers (Simple & Fast)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ Gyanjyoti AI Tutor Active Hai!\n\nMain aapki madad ke liye taiyar hoon.")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    if "Homework" in message.text:
        bot.reply_to(message, "📚 Homework portal update ho gaya hai.")
    else:
        bot.reply_to(message, "Aapka message mil gaya! Main jald hi reply karunga.")

# 3. Webhook Engine
@app.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook_check():
    # Forceful Webhook Registration
    url = f"https://api.telegram.org/bot{API_TOKEN}/setWebhook?url=https://gyanjyoti-smart-bot-final.onrender.com/{API_TOKEN}"
    requests.get(url) 
    return "<h1>Gyanjyoti Bot: Connection Forced & Running! ✅</h1>", 200

# 4. Starting Everything
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
