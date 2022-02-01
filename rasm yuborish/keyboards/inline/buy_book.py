from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

book_keys=InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🔍Eng yaqin do'konni topish", callback_data="mylocation"),
        InlineKeyboardButton(text="📨Kontakt ulashish", callback_data="mycontact")
    ]]
)