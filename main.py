import telebot
from flask import Flask, request

TOKEN = "8181288340:AAG8JEa2GXGstmgt1yzCrBJzhCkEweiBtl0"
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
    return '🤖 IQsmart bot is live on Render!'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Hello! IQsmart bot is now running 24/7 on Render with GitHub deployment! 🔥")

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=f"https://iqchats.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=10000)
