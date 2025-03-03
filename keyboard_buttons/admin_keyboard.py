from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foydalanuvchilar soni"),
            KeyboardButton(text="Reklama yuborish"),
        ],
        [   KeyboardButton(text="Kanal qo'shish"),
            KeyboardButton(text="Kanal o'chirish"),]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           KeyboardButtonRequestChat,KeyboardButtonRequestUser)
get_id = ReplyKeyboardMarkup(
    keyboard=[
[KeyboardButton(text="👥 Group",request_chat=KeyboardButtonRequestChat(request_id=125,chat_is_channel=False)),KeyboardButton(text="📢 Channel",request_chat=KeyboardButtonRequestChat(request_id=126,chat_is_channel=True))],
    ],resize_keyboard=True,
)