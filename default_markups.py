from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
     [
         KeyboardButton(text='Главное меню'),
     ],
    [
        KeyboardButton(text='Курс криптовалюты'),
    ],
    [
        KeyboardButton(text='Помощь')
    ]
    ]
)