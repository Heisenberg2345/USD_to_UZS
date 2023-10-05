import telebot
import requests
BOT_TOKEN = '6351544181:AAHQIc9TunqR1IXCRUAuOR-OBV5_eimOHak'
API_KEY = 'aadb12a34d5d4ea3898f7222030381b2'

bot = telebot.TeleBot(BOT_TOKEN)


def send_currency(chat_id):
    url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        usd_to_uzs = data['rates']['UZS']
        usd_to_rub = data['rates']['RUB']
        rub_to_uzs = usd_to_uzs/usd_to_rub
        message = f"1 доллар = {round(usd_to_uzs, 2)} сумов \n 1 рубль = {round(rub_to_uzs, 2)} сума"
        bot.send_message(chat_id, message)
    else:
        bot.send_message(chat_id,'Извините,данные отсутствуют.Попробуйте позже...')
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    send_currency(chat_id)
bot.polling()
