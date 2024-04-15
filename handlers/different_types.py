from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.undefined)
async def handler_debug(message: Message) -> None:
    await message.answer('xz')


@router.message(F.text)
async def handler_message_text(message: Message) -> None:
    print(F.__class__)
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