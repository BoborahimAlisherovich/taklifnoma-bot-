from typing import Union
from aiogram.enums.chat_member_status import ChatMemberStatus
from loader import bot


async def check(user_id, channel: Union[int, str]):
    
    member = await bot.get_chat_member(user_id=user_id, chat_id=channel)
    
    return member.status == ChatMemberStatus.MEMBER or (member.status==ChatMemberStatus.CREATOR) or (member.status==ChatMemberStatus.ADMINISTRATOR)