import telebot
from flask import Flask, request
import os
import threading

# ===== Bot Token (BotFather se mila hua) =====
API_TOKEN = "8676020356:AAFz-kraG7h2cltotemx63KVD8RCFPNltO8"
                     

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

# ===== /start command =====
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "Namaskar! Gyanjyoti AI Tutor active hai.\nHomework, Notice ya Contact likhkar bhejiye."
    )

# ===== All messages handler =====
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    msg_text = message.text.strip()

    if "Homework" in msg_text:
        bot.reply_to(message, "📚 Aaj ka homework update ho gaya hai.")
    elif "Notice" in msg_text:
        bot.reply_to(message, "📢 Naya notice check kiya ja raha hai.")
    elif "Contact" in msg_text:
        bot.reply_to(message, "📞 School Contact: +91-XXXXXXXXXX")
    else:
        bot.reply_to(
            message,
            "Main samajh gaya. Aap Homework, Notice ya Contact likh sakte hain."
        )

# ===== Webhook endpoint (Render ke liye) =====
@app.route('/' + API_TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK", 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(
        url='https://' + os.environ.get('RENDER_EXTERNAL_HOSTNAME') + '/' + API_TOKEN
    )
    return "Gyanjyoti Bot is Running", 200

# ===== Run bot polling =====
def run_bot():
    bot.infinity_polling(skip_pending=True)

# ===== Main =====
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
