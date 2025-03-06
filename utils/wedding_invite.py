import aiohttp
from aiogram import Bot
from datetime import datetime
import re

pattern = r"^(\d{2})\.(\d{2})\.(\d{4})$"

API_URL = " https://botlar.navetk.uz//invite/create/"
PROVIDER_KEY = "hubbun-nikah"





async def create_invite(bot: Bot, telegram_id: int, grooms_name: str, brides_name: str, 
                        wedding_date: str, full_address: str, latitude: float, longitude: float, 
                        description: str):
    """Bot orqali to‘y taklifnomasini yaratish."""

    data = {
        "telegram_id": telegram_id,
        "grooms_name": grooms_name,
        "brides_name": brides_name,
        "wedding_date": wedding_date,
        "full_address": full_address,
        "latitude": latitude,
        "longitude": longitude,
        "description": description
    }

    headers = {"Provider-Key": PROVIDER_KEY}

    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, json=data, headers=headers) as response:
            result = await response.json()
            
            if response.status in [200, 201]:
                message = f"✅ Taklifnoma yaratildi!\n\n📍 <a href='{result['data']['google_maps_link']}'>Google Xarita</a>\n🔗 <a href='{result['detail_url']}'>To‘liq ma’lumot</a>"
            else:
                message = f"❌ Xatolik yuz berdi: {result.get('error', 'Noma’lum xato')}"

            await bot.send_message(telegram_id, message, parse_mode="HTML")

def is_valid_date(date_str):
    
    match = re.match(pattern, date_str)
    if not match:
        return False  # Format noto'g'ri bo'lsa

    day, month, year = map(int, match.groups())

    try:
        # datetime module orqali to'g'ri sana ekanligini tekshiramiz
        datetime(year, month, day)
        return True
    except ValueError:
        return False  # Noto'g'ri sana (masalan, 30-fevral) bo'lsa
