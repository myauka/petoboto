import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from aiogram.dispatcher.filters import Command, Text
from default_markups import menu
from inline_markups import currencies1, currencies2, pnext
from config import BOT_TOKEN
from data_retrieval import data

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(Command('start'))
async def send_welcome(message: Message):
    await message.reply(text="<b>Приветствую тебя!</b>\n"
                        "\nЯ — бот для проверки текущего курса криптовалют\n"
                        "\nНапиши /help "
                        "чтобы узнать больше",
                        reply_markup=menu)


@dp.message_handler(Command('help'))
async def send_help(message: Message):
    await message.answer('/currencies\n'
                         '<b>Текущий курс данной валюты</b>\n')


@dp.message_handler(Command('currencies'))
async def show_currencies(message: Message):
    await message.answer(text='<b><i>Выберите криптовалюту</i></b>', reply_markup=currencies1)


async def update_text(message: types.Message):
    await message.edit_text(text='<b><i>Выберите криптовалюту</i></b>', reply_markup=currencies2)


@dp.message_handler(Text(equals=['Главное меню', 'Курс криптовалюты', 'Помощь']))
async def keyboard_menu(message: Message):
    if message.text == 'Главное меню':
        await send_welcome(message=message)
    if message.text == 'Курс криптовалюты':
        await show_currencies(message=message)
    if message.text == 'Помощь':
        await send_help(message=message)


@dp.callback_query_handler(text='BTC')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO BTC: {}'.format(data['UAH']['BTC']))


@dp.callback_query_handler(text='LTC')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO LTC: {}'.format(data['UAH']['LTC']))


@dp.callback_query_handler(text='DASH')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO DASH: {}'.format(data['UAH']['DASH']))


@dp.callback_query_handler(text='TRX')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO TRX: {}'.format(data['UAH']['TRX']))


@dp.callback_query_handler(text='ETH')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO ETH: {}'.format(data['UAH']['ETH']))


@dp.callback_query_handler(text='ZEC')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO ZEC: {}'.format(data['UAH']['ZEC']))


@dp.callback_query_handler(text='UNI')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO UNI: {}'.format(data['UAH']['UNI']))


@dp.callback_query_handler(text='USDT')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO USDT: {}'.format(data['UAH']['USDT']))


@dp.callback_query_handler(text='XLM')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO XLM: {}'.format(data['UAH']['XLM']))


@dp.callback_query_handler(text='WAVES')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO WAVES: {}'.format(data['UAH']['WAVES']))


@dp.callback_query_handler(text='LINK')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO LINK: {}'.format(data['UAH']['LINK']))


@dp.callback_query_handler(text='USDC')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO USDC: {}'.format(data['UAH']['USDC']))


@dp.callback_query_handler(text='EOS')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO EOS: {}'.format(data['UAH']['EOS']))


@dp.callback_query_handler(text='BNB')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO BNB: {}'.format(data['UAH']['BNB']))


@dp.callback_query_handler(text='XRP')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO XPR: {}'.format(data['UAH']['XRP']))


@dp.callback_query_handler(text='XEM')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO XEM: {}'.format(data['UAH']['XEM']))


@dp.callback_query_handler(text='DAI')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('UAH TO DAI: {}'.format(data['UAH']['DAI']))


@dp.callback_query_handler(text='next')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await update_text(call.message)


@dp.callback_query_handler(text='back')
async def BTC_currency(call: types.CallbackQuery):
    await call.answer(cache_time=60)
    await show_currencies(call.message)


@dp.callback_query_handler(text='close')
async def close_keyboard(call: types.CallbackQuery):
    await call.message.delete()
    # await call.message.edit_reply_markup(reply_markup=None)

# @dp.callback_query_handler(text='next')
# async def next_page(call: types.CallbackQuery):
#     await call.message.answer(text='<b><i>Выберите криптовалюту</i></b>', reply_markup=pnext)


if __name__ == '__main__':
    executor.start_polling(dp)