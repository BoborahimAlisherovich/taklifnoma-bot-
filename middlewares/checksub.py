from aiogram.dispatcher.middlewares.base import BaseMiddleware
from keyboard_buttons.subscription import check_button
from aiogram.types import ReplyKeyboardRemove
from utils import subscriptions
from loader import bot, db

from aiogram.types import Update
from typing import Callable, Dict, Any, Awaitable



class BigBrother(BaseMiddleware):
    async def __call__(
        self, 
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]], 
        event: Update, 
        data: Dict[str, Any]
    ) -> Any:
        
        CHANNELS = db.select_all_channels()

        if event.message:
            user = event.message.from_user.id
            if event.message.text in ['/start']:
                return await handler(event, data)
        elif event.callback_query:
            user = event.callback_query.from_user.id
            if event.callback_query.data == "check_subs":
                return await handler(event, data)
        else:
            return await handler(event, data)

        join_channel = []
        result = "Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling:\n"
        final_status = True

        for channel_id in CHANNELS:
            status = await subscriptions.check(user_id=user, channel=channel_id[0])
            final_status *= status
            channel = await bot.get_chat(channel_id[0])
            invite_link = await channel.export_invite_link()

            channel_info = [invite_link, channel.title, int(status)]
            join_channel.append(channel_info)
            print(status)
            if not status:
                result += f"👉 <a href='{invite_link}'>{channel.title}</a>\n"

        if not final_status:
            if event.message:
                await event.message.answer(
                    "Kanallarga to'liq obuna bo'ling", reply_markup=ReplyKeyboardRemove()
                )
                await event.message.answer(
                    result, disable_web_page_preview=True, reply_markup=check_button(join_channel),parse_mode="HTML"
                )
            return None

        return await handler(event, data)
