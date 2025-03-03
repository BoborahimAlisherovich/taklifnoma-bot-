from filters.check_sub_channel import IsCheckSubChannels
from loader import bot,db,dp,ADMINS
from aiogram.types import Message,InlineKeyboardButton
from aiogram.filters import Command
from filters.admin import IsBotAdminFilter
from states.reklama import Adverts,Channel
from aiogram.fsm.context import FSMContext #new
from keyboard_buttons import admin_keyboard
import time 
from aiogram import F


@dp.message(Command("admin"),IsBotAdminFilter(ADMINS))
async def is_admin(message:Message):
    await message.answer(text="Admin menu",reply_markup=admin_keyboard.admin_button)


@dp.message(F.text=="Foydalanuvchilar soni",IsBotAdminFilter(ADMINS))
async def users_count(message:Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

@dp.message(F.text=="Reklama yuborish",IsBotAdminFilter(ADMINS))
async def advert_dp(message:Message,state:FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")

@dp.message(Adverts.adverts)
async def send_advert(message:Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0],from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.01)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()

@dp.message(F.text=="Kanal o'chirish",IsBotAdminFilter(ADMINS))
async def channel_delete(message:Message,state:FSMContext):
    db.delete_channels()
    await state.clear()
    text = "Majburiy obuna kanallari o'chirildi."
    await message.answer(text,reply_markup=admin_keyboard.admin_button)

@dp.message(F.text=="Kanal qo'shish",IsBotAdminFilter(ADMINS))
async def channel_add(message:Message,state:FSMContext):
    await state.set_state(Channel.add)
    await message.answer(text="Qo'shish uchun kanal tanlang",reply_markup=admin_keyboard.get_id)

@dp.message(F.chat_shared,Channel.add)
async def add_channel(message: Message,state:FSMContext):
    id = message.chat_shared.chat_id
    try:
        
        chan = await bot.get_chat(id)
        channel_name = chan.full_name
        print(channel_name)

        text = "Kanal muvaffaqiyatli qo'shildi"
        db.add_channel(channel_id=int(id),channel_name=channel_name)
        
    except Exception as e:
        if str(e)=="UNIQUE constraint failed: CHANNELS.channel_id":
            text = "Ushbu kanal allaqachon qo'shilgan"
        else:
            text = "Botni kanalga admin qilishingiz kerak"
    await state.clear()
    await message.answer(text,reply_markup=admin_keyboard.admin_button)


# @dp.message_handler(state="kanal_qoshish", user_id=ADMINS, content_types=types.ContentTypes.ANY)
# async def send_ad_to_all(message: types.Message, state = FSMContext):
#     # print(message)
#     try:
#         if message.forward_from_chat:
#             # print(message.forward_from_chat.id)
#             id = message.forward_from_chat.id
#             name = message.forward_from_chat.title
#             chat = await bot.get_chat(id)
            
#         elif message.text:
#             chanel = await bot.get_chat(message.text)
#             # print(chanel)
#             id = chanel.id
#             invite_link = await chanel.export_invite_link()
#             name = chanel.full_name
#         else:
#             await message.answer("Nimadir xato ketti")
        
#         await bot.get_chat_member(id, message.from_user.id)
#         text = f"Name: {name}\n"
#         text += f"Link: {invite_link}\n"
#         text += f"\nQo'shildi ✅\n"
#         await db.add_chanel(id, name, invite_link)
#         await message.answer(text,reply_markup=admin_main_2)
#     except Exception as err:
#         await message.answer(f"Oldin botni kanal yoki guruhga qo'shing, so'ngra qaytadan urinib ko'ring.\n\nYoki bot linki to'g'riligiga e'tibor bering: {err}",reply_markup=admin_main_2)
#     await state.finish()