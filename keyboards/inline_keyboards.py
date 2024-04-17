from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_start_config() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text='Да!', callback_data='get_start_yes'),
            InlineKeyboardButton(text='Очень интересно!', callback_data='get_start_yes')
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


def get_webapp_config() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="Тык", web_app=WebAppInfo(url=f'https://r0lton.github.io/TicTacToe/')),
                                 # callback_data='get_webapp'),
            InlineKeyboardButton(text='Назад', callback_data='menu')
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


def get_BMSTU_config() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text='Ссылка1', url='https://www.google.ru/?hl=ru'),
            InlineKeyboardButton(text='Ссылка2', url='https://www.google.ru/?hl=ru')
        ],
        [
            InlineKeyboardButton(text='Ссылка3', url='https://www.google.ru/?hl=ru'),
            InlineKeyboardButton(text='Ссылка4', url='https://www.google.ru/?hl=ru')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='menu')
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard

