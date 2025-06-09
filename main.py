import telebot
from flask import Flask, request

TOKEN = "8173735133:AAHd6O5DVgLSNiDd67XT8mrPxUcCWaQM2IM"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'ok', 200

@app.route('/')
def index():
    return '🤖 Botx is alive!'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Hello! Botx is now running 24/7 on Render! 🚀")

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f"https://botx.onrender.com/{TOKEN}")
    app.run(host='0.0.0.0', port=10000)
