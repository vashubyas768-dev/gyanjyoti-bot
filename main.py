import telebot
from flask import Flask, request
import os
import time

# 1. Bot Setup
# Dhyan dein: Yahan apna Token check kar lein
API_TOKEN = '8676020356:AAFz-kraG7h2cltotemx63KVD8RCFPNltO8' 
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# 2. Welcome Message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ Namaskar! Gyanjyoti Smart School Bot ab live hai.\n\nAap niche diye gaye buttons ka use kar sakte hain.")

# 3. Message Handlers
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    msg = message.text
    if "Homework" in msg:
        bot.reply_to(message, "📚 Aaj ka homework update ho gaya hai. Diary check karein.")
    elif "Results" in msg:
        bot.reply_to(message, "📊 Results portal par upload ho chuke hain.")
    elif "Notice" in msg:
        bot.reply_to(message, "📢 Naya notice board par check karein.")
    elif "Contact" in msg:
        bot.reply_to(message, "📞 School Office: [Yahan Number Likhein]")
    else:
        bot.reply_to(message, "Kripya 'Homework' ya 'Notice' likhein.")

# 4. Webhook Logic (Expert Configuration)
@app.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook_status():
    # Jab aap browser mein link kholenge toh ye dikhega
    return "<h1>Gyanjyoti Bot Status: Online ✅</h1>", 200

# 5. AUTO-CONNECT (Ye hissa Telegram ko Render se jodta hai)
def set_webhook():
    time.sleep(2) # Server ko start hone ka time de raha hai
    bot.remove_webhook()
    time.sleep(1)
    # Aapka exact Render URL
    render_url = 'https://gyanjyoti-smart-bot-final.onrender.com/' + API_TOKEN
    bot.set_webhook(url=render_url)

# 6. Main Execution
if __name__ == "__main__":
    set_webhook() # Start hote hi connection banayega
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
