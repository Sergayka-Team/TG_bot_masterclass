from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.markdown import hbold

from keyboards.inline_keyboards import get_webapp_config, get_BMSTU_config

router = Router()


@router.message(F.text == "WebApp")
async def handler_text_WebApp(message: Message) -> None:
    await message.answer(f'Отлично, что ты хочешь узнать про технологию WebApp',
                         reply_markup=ReplyKeyboardRemove())
    # f'Тогда давай без лишних слов, просто {hbold("тыкни")}',
    # reply_markup=get_webapp_config())

    await message.answer(f'Тогда давай без лишних слов, просто {hbold("тыкни")}',
                         reply_markup=get_webapp_config())


@router.message(F.text == "КФ МГТУ")
async def handler_text_BMST(message: Message) -> None:
    await message.answer(f'Тут ты сможешь узнать актуальную информацию про наш филиал',
                         reply_markup=ReplyKeyboardRemove())

    await message.answer(f'Какой-то текст / дискриптион',
                         reply_markup=get_BMSTU_config())


@router.message(F.text == "Я закончил!")
async def handler_text_end(message: Message) -> None:
    await message.answer(f'Отлично! Ты посмотрел как этот бот выглядит снаружи, '
                         f'теперь давай окунемся в его код!',
                         reply_markup=ReplyKeyboardRemove())


@router.message(F.undefined)
async def handler_debug(message: Message) -> None:
    await message.answer('xz')


@router.message(F.text)
async def handler_message_text(message: Message) -> None:
    await message.answer(f'{message.from_user.full_name}, ты отправил текст')


@router.message(F.sticker)
async def handler_message_sticker(message: Message) -> None:
    await message.answer(f'{message.from_user.full_name}, ты отправил стикер')


@router.message(F.animation)
async def handler_message_gif(message: Message) -> None:
    await message.answer(f'{message.from_user.full_name}, ты мне нахуя-то отправил гифку')


@router.message(F.photo)
async def handler_message_photo(message: Message) -> None:
    await message.answer('photo')


@router.message(F.document)
async def handler_message_doc(message: Message) -> None:
    await message.answer('doc')


@router.message(F.location)
async def handler_message_geo(message: Message) -> None:
    await message.answer('geo')


@router.message(F.emoji)
async def handler_message_emoji(message: Message) -> None:
    await message.answer('emoji')


@router.message(F.audio)
async def handler_message_audio(message: Message) -> None:
    await message.answer('audio')