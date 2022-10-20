from flask import Flask, request
from settings import telegram, telegram_url

app = Flask(__name__)

from telebot import types
@app.route('/{}'.format(telegram_url), methods=["POST"])
def webhook():
    telegram.process_new_updates([types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200


@telegram.message_handler(commands=['start', 'help'])
def startCommand(message):
    command.take_commands(message=telegram.send_message, id=message.chat.id, from_id=message.from_user.id, text="/помощь")

import command
@telegram.message_handler(content_types='text')
def message_reply(message):
    try:
        id=message.chat.id
        from_id=message.from_user.id
        text=message.text

        if text != "":
            command.take_commands(message=telegram.send_message, id=id, from_id=from_id, text=text)
    except Exception as e:
        telegram.send_message(id, e)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
