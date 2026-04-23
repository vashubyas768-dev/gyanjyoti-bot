import telebot
from flask import Flask, request
import os
import requests

# 1. Bot Setup
API_TOKEN = '8676020356:AAFz-kraG7h2cltotemx63KVD8RCFPNltO8'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# 2. Handlers (Direct Answers & Solutions)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ Gyanjyoti AI Tutor Active Hai!\n\nMain Sivasagar ke schools ke liye taiyar hoon. Aap 'Homework' ya 'Results' button check kar sakte hain.")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    # User Correction: Providing direct solutions alongside explanations
    if "Homework" in message.text:
        bot.reply_to(message, "📚 Homework Section: Aapka homework portal update ho gaya hai. Yahan direct solutions aur methods dono milenge.")
    elif "Results" in message.text:
        bot.reply_to(message, "📊 Results: Digital marksheets taiyar ho rahi hain.")
    else:
        bot.reply_to(message, "Aapka message mil gaya! Main jald hi step-by-step reply karunga.")

# 3. Webhook Engine with Auto-Cleaner
@app.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook_check():
    # Forceful Webhook Registration & Cleaning purane pending messages
    webhook_url = f"https://gyanjyoti-smart-bot-final.onrender.com/{API_TOKEN}"
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)
    return "<h1>Gyanjyoti Bot: Connection Forced & Running! ✅</h1>", 200

# 4. Running the server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
