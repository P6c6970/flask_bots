from flask import Flask, request
from settings import telegram, telegram_url

app = Flask(__name__)

from telebot import types


@app.route('/{}'.format(telegram_url), methods=["POST"])
def webhook():
    telegram.telegram.process_new_updates([types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200


@telegram.telegram.message_handler(commands=['start', 'help'])
def startCommand(message):
    processing.take_commands(messenger=telegram, id=message.chat.id, from_id=message.from_user.id, text="/помощь")


import processing


@telegram.telegram.message_handler(content_types='text')
def message_reply(message):
    try:
        id = message.chat.id
        from_id = message.from_user.id
        text = message.text
        print(f"USER {id} printed {text}")

        if text != "":
            processing.take_commands(messenger=telegram, id=id, from_id=from_id, text=text)
    except Exception as e:
        if e[:19] != "HTTPSConnectionPool":
            telegram.message(id, e)

@telegram.telegram.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            from_id = call.message.chat.id
            id = call.message.from_user.id
            text = call.data
            print(f"USER {from_id} called {text}")

            if text != "":
                processing.take_commands_call(messenger=telegram, id=id, from_id=from_id, text=text)
    except Exception as e:
        if e[:19] != "HTTPSConnectionPool":
            telegram.message(id, f"Callback {e}")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
