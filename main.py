import telebot
from flask import Flask, request
import os

# 1. Bot Setup
# Dhyan dein: Yahan apna pura API Token rehne dein
API_TOKEN = '8676020356:AAFz-kraG7h2cltotemx63KVD8RCFPNltO8' 
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# 2. Welcome Message
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaskar! Gyanjyoti Smart School Bot active hai. Main aapki kya madad kar sakta hoon?")

# 3. Simple Replies
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    msg = message.text
    if "Homework" in msg:
        bot.reply_to(message, "📚 Aaj ka homework update ho gaya hai.")
    elif "Notice" in msg:
        bot.reply_to(message, "📢 Naya notice board par check karein.")
    elif "Contact" in msg:
        bot.reply_to(message, "📞 School Contact: [Apna Number Daalein]")
    else:
        bot.reply_to(message, "Aap 'Homework' ya 'Notice' likhkar puch sakte hain.")

# 4. Render Webhook Engine
@app.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook_status():
    return "Gyanjyoti Bot is Running!", 200

# 5. AUTO-CONNECT LOGIC (Ye lines bot ko chalu karengi)
bot.remove_webhook()
bot.set_webhook(url='https://gyanjyoti-smart-bot-final.onrender.com/' + API_TOKEN)

# 6. Starting Everything
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
