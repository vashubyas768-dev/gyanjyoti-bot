import telebot
from flask import Flask, request
import os

# 1. Bot Setup
API_TOKEN = '8676020356:AAFz-kraG7h2cltotemx63KVD8RCFPNltO8' # Apna pura Token yahan rehne dein
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# 2. Welcome Message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaskar! Gyanjyoti Smart School Bot active hai.")

# 3. Simple Replies
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    msg = message.text
    if "Homework" in msg:
        bot.reply_to(message, "📚 Aaj ka homework update ho gaya hai.")
    elif "Notice" in msg:
        bot.reply_to(message, "📢 Naya notice board par check karein.")
    else:
        bot.reply_to(message, "Aap 'Homework' ya 'Notice' likhkar puch sakte hain.")

# 4. Render Webhook Engine (Conflict se bachne ke liye polling hata di gayi hai)
@app.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    render_url = 'https://' + os.environ.get('RENDER_EXTERNAL_HOSTNAME') + '/' + API_TOKEN
    bot.set_webhook(url=render_url)
    return "Bot is Running!", 200

# 5. Starting Everything
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
