from loader import dp,ADMINS
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F
from states.reklama import Toy
from aiogram.fsm.context import FSMContext #new
from keyboard_buttons.taklifnoma_button import location_button
from utils.wedding_invite import create_invite, is_valid_date
from datetime import datetime
from data.config import DOMAIN_NAME
from aiogram.types import WebAppInfo



@dp.message(F.text=="Taklifnoma yaratish")
async def taklifnoma_boshlash(message:Message,state:FSMContext):
    text = "Kuyov ismini kiriting: "
    await state.set_state(Toy.grooms_name)
    await message.answer(text)

@dp.message(F.text,Toy.grooms_name)
async def get_grooms_name(message:Message,state:FSMContext):
    await state.update_data({"grooms_name":message.text})
    text = "Kelin ismini kiriting: "
    await state.set_state(Toy.brides_name)
    await message.answer(text)

@dp.message(F.text,Toy.brides_name)
async def get_brides_name(message:Message,state:FSMContext):
    await state.update_data({"brides_name":message.text})
    text = """📅 To‘y sanasini kiriting (kun.oy.yil shaklida):
🔹 Masalan: 31.12.2030 """
    await state.set_state(Toy.wedding_date)
    await message.answer(text)

@dp.message(F.text,Toy.wedding_date)
async def get_wedding_date(message:Message,state:FSMContext):
    if is_valid_date(message.text):
        wedding_date = datetime.strptime(message.text, "%d.%m.%Y").strftime("%Y-%m-%d")
        print(wedding_date)
        await state.update_data({"wedding_date":str(wedding_date)})
        text = "To'liq manzilni kiriting: "
        await state.set_state(Toy.full_address)
        await message.answer(text)
    else:
        text = """📅 To‘y sanasi xato kiritildi. To'g'ri shaklda kiriting (kun.oy.yil shaklida):
🔹 Masalan: 31.12.2030 """
        await message.answer(text)


@dp.message(F.text,Toy.full_address)
async def get_full_address(message:Message,state:FSMContext):
    await state.update_data({"full_address":message.text})
    text = "lokatsiya yuboring: "
    await state.set_state(Toy.location)
    await message.answer(text=text,reply_markup=location_button)

@dp.message(F.location,Toy.location)
async def get_location(message:Message,state:FSMContext):
    latitude = message.location.latitude
    longitude = message.location.longitude
    await state.update_data({"latitude":latitude})
    await state.update_data({"longitude":longitude})
    text = "To'y xaqida batafsil ma'lumot yozing: "
    await state.set_state(Toy.description)
    await message.answer(text)

@dp.message(F.text,Toy.description)
async def get_description(message:Message,state:FSMContext):
    data = await state.get_data()
    grooms_name = data.get("grooms_name")
    brides_name = data.get("brides_name")
    wedding_date = data.get("wedding_date")
    full_address = data.get("full_address")
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    description = message.text
    telegram_id = message.from_user.id
    await create_invite(
            bot=message.bot, 
            telegram_id=telegram_id,
            grooms_name=grooms_name,
            brides_name=brides_name,
            wedding_date=wedding_date,
            full_address=full_address,
            latitude=latitude,
            longitude=longitude,
            description=description
        )
    await state.clear()
    

    photo_url = "https://i.ibb.co/MxpRcpBT/wed.jpg"
    invite_url = f"https://{DOMAIN_NAME}/invite/{telegram_id}/"
    text = f"💌 <b>Sizning to‘y <a href='{invite_url} 💍'>taklifnoma</a>ngiz!</b>\n\n"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📨 Taklifnomani ko‘rish", web_app=WebAppInfo(url=invite_url) )],
        [InlineKeyboardButton(text="📤 Boshqalarga ulashish", switch_inline_query=invite_url)]
    ])

    await message.answer_photo(photo=photo_url,caption=text, reply_markup=keyboard, parse_mode="HTML")



