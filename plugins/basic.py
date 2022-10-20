def repeat(message, id, text):
    message(id, text)


def reverse(message, id, text):
    message(id, text[::-1])


def repeat_fun(**kwargs):
    repeat(kwargs['message'], kwargs['from_id'], kwargs['text'][9:])


def reverse_fun(**kwargs):
    repeat(kwargs['message'], kwargs['from_id'], kwargs['text'][11:])


commands = [
    (r'/повтори [\S\s]+[\S]+', repeat_fun, "/повтори {текст} - возвращает текст"),
    (r'/переверни [\S\s]+[\S]+', reverse_fun, "/переверни {текст} - возвращает перевернутый текст"),
]
