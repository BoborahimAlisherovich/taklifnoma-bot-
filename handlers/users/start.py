from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons.taklifnoma_button import taklifnoma

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    text = """💌 Assalomu alaykum!

Siz onlayn to‘y taklifnomasi yaratish uchun botdasiz! 🎉

📜 Bot yordamida siz:
✅ Kelin va kuyov ismini kiritib, taklifnoma yaratishingiz
📅 Sana va joylashuv qo‘shishingiz
📲 Web App orqali taklifnomani ko‘rishingiz va yuklab olishingiz mumkin.

🔹 Taklifnoma yaratish uchun:
👉 "Taklifnoma yaratish" tugmasini bosing!

📩 Savollar bo‘lsa, biz bilan bog‘laning!"""
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
    except:
        pass
    await message.answer(text=text,reply_markup=taklifnoma)
