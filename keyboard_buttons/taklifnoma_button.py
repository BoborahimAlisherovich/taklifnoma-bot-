from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup,WebAppInfo,WebAppData

taklifnoma = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Taklifnoma yaratish"),
        ],   
    ],
   resize_keyboard=True,
   input_field_placeholder="Taklifnoma yaratish uchun tugmani bosing..."
)

location_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Manzil yuborish", request_location=True),
        ],   
    ],
   resize_keyboard=True,
)
 