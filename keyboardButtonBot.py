from aiogram.types import ReplyKeyboardRemove,\
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_hi = KeyboardButton('Показания счетчиков')

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button_hi)