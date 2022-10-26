def repeat_fun(**kwargs):
    kwargs["messenger"].message(kwargs['from_id'], kwargs['text'][9:])


def reverse_fun(**kwargs):
    kwargs["messenger"].message(kwargs['from_id'], kwargs['text'][:10:-1])


from packages.keyboard import Keyboard, Button


def get_keyboard(**kwargs):
    keyboard = Keyboard([
        [Button("/клавиатура"), Button("/помощь")],
        [Button("/удалить клавиатуру")],
    ])
    kwargs["messenger"].message(kwargs["id"], f"Клавиатура",
                                keyboard=keyboard.get(kwargs["messenger"].get_type()))


def delete_keyboard(**kwargs):
    kwargs["messenger"].message(kwargs["id"], f"Клавиатура удалена",
                                keyboard=Keyboard.delete_keyboard(kwargs["messenger"].get_type()))


from packages.command import Command

commands = [
    Command(r'/повтори [\S\s]+[\S]+', repeat_fun, "/повтори {текст} - возвращает текст"),
    Command(r'/переверни [\S\s]+[\S]+', reverse_fun, "/переверни {текст} - возвращает перевернутый текст"),
    Command('/клавиатура', get_keyboard),
    Command('/удалить клавиатуру', delete_keyboard),
]
