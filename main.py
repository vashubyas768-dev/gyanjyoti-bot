import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Logging setup taaki server par status dikhta rahe
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# 1. Aapka Telegram Token aur Bachon ka Data
BOT_TOKEN = "8653944194:AAFl578Ww7LQkN5_YH2GGLUsb3awAR0ol18"

STUDENT_DATA = {
    "101": {"name": "Arnob Gogoi", "roll": "101", "class": "6", "marks": "85", "status": "Pass"},
    "102": {"name": "Bikram Borah", "roll": "102", "class": "6", "marks": "42", "status": "Pass"},
    "103": {"name": "Dimpi Dihingia", "roll": "103", "class": "6", "marks": "78", "status": "Pass"},
    "104": {"name": "Gaurav Chutia", "roll": "104", "class": "6", "marks": "29", "status": "Fail"},
    "105": {"name": "Jaanmoni Saikia", "roll": "105", "class": "6", "marks": "92", "status": "Pass"}
}

# 2. Start Command Response
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_msg = (
        "✨ *Gyanjyoti AI Tutor System Live Hai!* ✨\n\n"
        "Apna Result dekhne ke liye krpya apna *Roll Number* bheinjein.\n"
        "उदाहरण: `101` ya `105`"
    )
    await update.message.reply_text(welcome_msg, parse_mode="Markdown")

# 3. Result Filter aur Reply Logic
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_input = update.message.text.strip()
    
    if user_input in STUDENT_DATA:
        student = STUDENT_DATA[user_input]
        
        # Pass/Fail ke liye emoji setup
        status_emoji = "✅" if student["status"] == "Pass" else "❌"
        
        result_msg = (
            "📝 *GYANJYOTI SMART SCHOOL - RESULT* 📝\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 *Student Name:* {student['name']}\n"
            f"🔢 *Roll Number:* {student['roll']}\n"
            f"📚 *Class:* {student['class']}\n"
            f"📊 *Total Marks:* {student['marks']}/100\n"
            f"📢 *Status:* {status_emoji} *{student['status']}*\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "👍 _Aapke ujjwal bhavishya ki kamna karte hain!_"
        )
        await update.message.reply_text(result_msg, parse_mode="Markdown")
    else:
        await update.message.reply_text(
            "⚠️ *Roll Number Nahi Mila!*\n"
            "Krpya sahi Roll Number bheinjein (Jaise: 101, 102, 103, 104, 105)."
        )

# 4. Main Function to Run Bot
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🤖 Gyanjyoti Bot successfully started...")
    app.run_polling()

if __name__ == '__main__':
    main()
