import json
import telebot

with open('config.json') as conf:
    config = json.load(conf)

bot = telebot.TeleBot(config['access_token'])


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
