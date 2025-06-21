import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from flask import Flask
from threading import Thread

TOKEN = os.getenv("7653506621:AAFzxI70OoygNImIP99tmjpB5GBr2c7pLZ0")  # Token dari ENV

app = Flask(__name__)

@app.route('/')
def home():
    return "WAFLEX+™ Aktif!"

def run():
    app.run(host='0.0.0.0', port=8080)

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📁 KONVERSI TXT ➜ VCF", callback_data='fitur1')],
        [InlineKeyboardButton("💰 HITUNG GAJI", callback_data='fitur2')],
        [InlineKeyboardButton("🌐 TRANSLATE CHINA", callback_data='fitur3')],
        [InlineKeyboardButton("♻️ RESET SISTEM", callback_data='fitur4')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Selamat datang di WAFLEX+™, pilih fitur:", reply_markup=reply_markup)

def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "fitur1":
        query.edit_message_text("📌 FITUR KONVERSI TXT ➜ VCF\n\nSilakan upload file .txt...")
    elif query.data == "fitur2":
        query.edit_message_text("📌 FITUR HITUNG GAJI\n\nPilih mata uang: 🇮🇩 IDR atau 🇺🇸 USD")
    elif query.data == "fitur3":
        query.edit_message_text("📌 FITUR TRANSLATE\n\nKetik kalimat yang ingin diterjemahkan.")
    elif query.data == "fitur4":
        query.edit_message_text("✅ Sistem berhasil direset.")

def echo_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if "upload" in text.lower():
        update.message.reply_text("📤 Contoh Translate:\n🇨🇳 示例翻译\n🇭🇰 示例翻譯\n🇺🇸 Example translation")
    else:
        update.message.reply_text(f"Kamu bilang: {text}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_handler))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo_handler))

    Thread(target=run).start()  # Flask keep-alive
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
