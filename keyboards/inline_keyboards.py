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
            InlineKeyboardButton(text="Тык", web_app=WebAppInfo(url=f'https://tic-tac-toe-sandy.vercel.app/')),
            InlineKeyboardButton(text='Назад', callback_data='menu')
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


def get_BMSTU_config() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text='Наша кафедра', url='https://kf.bmstu.ru/edu/kf/iuk/iuk2'),
            InlineKeyboardButton(text='Для абитуриентов', url='https://kf.bmstu.ru/priemnaya-komissiya')
        ],
        [
            InlineKeyboardButton(text='Наш TG', url='t.me/bmstu_kaluga'),
            InlineKeyboardButton(text='Наш ВК', url='https://vk.com/bmstu_kaluga')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='menu')
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


def get_finish_config() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text='Уже ознакомился!', callback_data="next"),
            InlineKeyboardButton(text="Сейчас попробую!", callback_data="test")
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard
