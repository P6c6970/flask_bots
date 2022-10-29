# -*- coding: utf-8 -*-
import re

from settings import plugins_list

command_text_list = None


def help_list(**kwargs):
    kwargs["messenger"].message(kwargs["id"], f"Вот команды которые я понимаю:\n{command_text_list}")


from packages.command import Command

commands = [
    Command('/помощь', help_list),
]

commands_call = [
]

for plugin_name in plugins_list:
    package_obj = __import__(f"plugins.{plugin_name}")
    module_obj = getattr(package_obj, plugin_name)
    commands += getattr(module_obj, "commands")
    if 'commands_call' in dir(module_obj):
        commands_call += getattr(module_obj, "commands_call")


def get_description_commands(commands):
    return [str(i) for i in commands if i.is_visible]  # list visible commands


command_text_list = '\n'.join(get_description_commands(commands))


def search_commands(commands, command):
    for i in commands:
        if re.fullmatch(i.text, command):
            return i.fun


def take_commands(**kwargs):
    fun = search_commands(commands, kwargs["text"])
    if fun is not None:
        fun(messenger=kwargs["messenger"], id=kwargs["id"], from_id=kwargs["from_id"], text=kwargs["text"])
    elif kwargs["id"] == kwargs["from_id"]:
        kwargs["messenger"].message(kwargs["id"], 'Ничего не понял')


# if re.fullmatch(regex_name, message):


def take_commands_call(**kwargs):
    fun = search_commands(commands_call, kwargs["text"])
    if fun is not None:
        fun(messenger=kwargs["messenger"], id=kwargs["id"], from_id=kwargs["from_id"], text=kwargs["text"])
    elif kwargs["id"] == kwargs["from_id"]:
        kwargs["messenger"].message(kwargs["id"], 'Ничего не понял')
