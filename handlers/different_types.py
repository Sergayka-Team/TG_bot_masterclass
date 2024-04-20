import asyncio

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.markdown import hbold, hitalic

from keyboards.inline_keyboards import get_webapp_config, get_BMSTU_config, get_finish_config

router = Router()


@router.message(F.text == "Игра")
async def handler_text_game(message: Message) -> None:
    await message.answer(text="Режим игры еще находится в разработке🤡",
                         show_alert=True)


@router.message(F.text == "WebApp")
async def handler_text_WebApp(message: Message) -> None:
    await message.answer(f'Отлично, что ты хочешь узнать про технологию WebApp🤪',
                         reply_markup=ReplyKeyboardRemove())

    await asyncio.sleep(1)

    await message.answer_sticker(r'CAACAgIAAxkBAAJRQ2YgbJOYXY_NZbdDGsmRxeO8cQc3AAIvRQACWh1BSGD3_PgXloUdNAQ')

    await asyncio.sleep(2)

    await message.answer(f'Тогда давай без лишних слов, просто {hbold("тыкни")}',
                         reply_markup=get_webapp_config())


@router.message(F.text == "Информация")
async def handler_text_BMST(message: Message) -> None:
    await message.answer(
        f"{hbold('Тут ты сможешь узнать актуальную информацию про Калужский Филиал МГТУ им. Н.Э.Баумана🙈')}",
        reply_markup=ReplyKeyboardRemove())

    await asyncio.sleep(2)

    await message.answer(f"Сейчас Вы находитесь на территории кафедры ИУК2 \"Информационные системы и сети\"\n"
                         f"Наш заведующий кафедры - Чухраев Игорь Владимирович\n\n"
                         f"{hbold('Выпускники кафедры ИУК2 «Информационные системы и сети»:')}\n"
                         f"{hitalic('-Приобретают навыки и опыт программирования разнообразных задач, осваивают несколько языков и сред программирования (С, C++, С#, Java, PHP, Python, VHDL, Go, UML, Assemblerи др.)')}\n"
                         f"{hitalic('-Свободно работают практически во всех современных операционных системах;')}\n"
                         f"{hitalic('-Программируют микропроцессорные системы, микроконтроллеры и ПЛИС;')}\n"
                         f"{hitalic('-Разрабатывают различные информационно-вычислительные системы, причем не только электронные схемы на современной элементной базе, но и схемы сопряжения с другими комплексами включая программное обеспечение для установки, настройки и эффективного функционирования всей системы в целом;')}\n"
                         f"{hitalic('-Получают навыки проектирования, прокладки, настройки и эксплуатации компьютерных сетей различной сложности и конфигурации.')}",
                         reply_markup=get_BMSTU_config())


@router.message(F.text == "Я закончил!")
async def handler_text_end(message: Message) -> None:
    await message.answer(f'А ты точно закончил? Еще есть команда /test',
                         reply_markup=get_finish_config())


@router.message(F.text)
async def handler_message_text(message: Message) -> None:
    await message.answer(f'Хммм... {message.text}🤔... глубокая мысль...')


@router.message(F.sticker)
async def handler_message_sticker(message: Message) -> None:
    await message.answer_sticker(r'CAACAgIAAxkBAAJRQGYgXczMch_6B7ea1Dxfrwr4V53pAAJ8NAACKZR5SKsBZBwDjNndNAQ')

    await asyncio.sleep(2)

    await message.answer(f'Круто! Теперь попробуй отправить любой файл (doc, pdf)')


@router.message(F.animation)
async def handler_message_gif(message: Message) -> None:
    await message.answer(f'Ты просто машина! Давай теперь напишем команду /help')


@router.message(F.photo)
async def handler_message_photo(message: Message) -> None:
    await message.answer('photo')


@router.message(F.document)
async def handler_message_doc(message: Message) -> None:
    await message.answer('Документ получен!😎\n'
                         'Теперь отправь мне гифку!')


@router.message(F.location)
async def handler_message_geo(message: Message) -> None:
    await message.answer('geo')


@router.message(F.emoji)
async def handler_message_emoji(message: Message) -> None:
    await message.answer('emoji')


@router.message(F.audio)
async def handler_message_audio(message: Message) -> None:
    await message.answer('audio')
