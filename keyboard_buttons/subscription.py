from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
# check_button = InlineKeyboardMarkup(
#     inline_keyboard=[[
#         InlineKeyboardButton(text="Obunani tekshirish", callback_data="check_subs")
#     ]]
# )

 
def check_button(channels):

    channels_check = InlineKeyboardBuilder()
    for channel in channels:
        if channel[2]==0:
            channels_check.row(InlineKeyboardButton(text=f"{channel[1]}", url=f"{channel[0]}"))
        else:
            channels_check.row(InlineKeyboardButton(text=f"✅{channel[1]}", url=f"{channel[0]}"))
    channels_check.row(InlineKeyboardButton(text="Obunani tekshirish ✅",url="https://t.me/Nikohuz_bot?start=help"))
        
    return channels_check.as_markup()