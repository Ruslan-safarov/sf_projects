import json

import requests
import telebot
from telebot import TeleBot

TOKEN = '5577412940:AAEOeeG8uTZrykbrm34gEtlBWlBwapiljq4'

bot: TeleBot = telebot.TeleBot(TOKEN)

keys = {
    'доллар': 'USD',
    'биткоин': 'BTC',
    'эфириум': 'ETH',
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду для бота в следубщем формате:\n<имя валюты>\
<в какую валюту перевести>\
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')


bot.polling()