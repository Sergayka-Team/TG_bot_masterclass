import asyncio

from aiogram import Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.reply_keyboard import get_main_menu

router = Router()


@router.callback_query(lambda callback: callback.data == 'get_start_yes')
async def callback_get_start_yes(callback: CallbackQuery) -> None:
    await callback.answer(cache_time=3)

    await callback.message.answer(text='Здорово! Тогда смотри какие функции у меня есть😎',
                                  reply_markup=get_main_menu(),
                                  show_alert=True)


@router.callback_query(lambda callback: callback.data == 'menu')
async def callback_menu(callback: CallbackQuery) -> None:
    await callback.answer(cache_time=3)

    await callback.message.answer(text='Ты вернулся в главное меню!',
                                  reply_markup=get_main_menu())


@router.callback_query(lambda callback: callback.data == 'get_webapp')
async def callback_webapp(callback: CallbackQuery) -> None:
    # Можно сделать крестики - нолики на Flask и подключить его через WepApp
    await callback.answer(
        text="Бот в режиме обслуживания :(\nПожалуйста, подождите",
        show_alert=True
    )


@router.callback_query(lambda callback: callback.data == "next")
async def callback_next(callback: CallbackQuery) -> None:
    await callback.message.answer(
        text='Круто!',
        reply_markup=ReplyKeyboardRemove()
    )

    await asyncio.sleep(1)

    await callback.message.answer_sticker(r'CAACAgIAAxkBAAJRPWYgXHGrRK0scClk16r6DniETdxBAAIdGgACIucJSAe9y5A0RJZyNAQ')

    await callback.message.answer(f'Ты посмотрел как этот бот выглядит снаружи, '
                                  f'теперь давай окунемся в его код!',
                                  reply_markup=ReplyKeyboardRemove())


@router.callback_query(lambda callback: callback.data == "test")
async def callback_test(callback: CallbackQuery) -> None:
    await callback.answer(
        text="Напиши команду /test",
        show_alert=True
    )


@router.callback_query()
async def any_callback(callback: CallbackQuery) -> None:
    await callback.answer(
        text="Бот в режиме обслуживания :(\nПожалуйста, подождите",
        show_alert=True
    )
