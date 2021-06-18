from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

currencies1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='BTC', callback_data='BTC')
        ],
        [
            InlineKeyboardButton(text='LTC', callback_data='LTC')
        ],
        [
            InlineKeyboardButton(text='DASH', callback_data='DASH'),
        ],
        [
            InlineKeyboardButton(text='TRX', callback_data='TRX'),
        ],
        [
            InlineKeyboardButton(text='ETH', callback_data='ETH'),
        ],
        [
            InlineKeyboardButton(text='ZEC', callback_data='ZEC'),

        ],
        [
            InlineKeyboardButton(text='UNI', callback_data='UNI'),
        ],
        [
            InlineKeyboardButton(text='➡️', callback_data='next')
        ],
        [
            InlineKeyboardButton(text='Закрыть', callback_data='close')
        ]
    ]
)

currencies2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='USDT', callback_data='USDT'),
            InlineKeyboardButton(text='XLM', callback_data='XLM'),
            InlineKeyboardButton(text='WAVES', callback_data='WAVES'),
            InlineKeyboardButton(text='LINK', callback_data='LINK'),
            InlineKeyboardButton(text='USDC', callback_data='USDC')
        ],
        [
            InlineKeyboardButton(text='⬅️', callback_data='back'),
        ],
        [
            InlineKeyboardButton(text='Закрыть', callback_data='close')
        ]
    ]

)

pnext = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='test', callback_data='')
        ]
    ]
)
