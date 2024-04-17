from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_main_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    # buttons = ["PyGame", "WepApp", "КФ МГТУ", "Я закончил!"]
    buttons = ["Игра", "WebApp", "Информация", "Я закончил!"]

    for button_text in buttons:
        keyboard.button(text=button_text)

    keyboard.adjust(3)

    keyboard = keyboard.as_markup(resize_keyboard=True)

    return keyboard


