from aiogram.types import BotCommandScopeChat

from loader import bot
from .admins import set_admins_commands  # noqa: F401
from .users import set_default_commands  # noqa: F401


async def remove_admins_commands(id: int):
    await bot.delete_my_commands(scope=BotCommandScopeChat(chat_id=id))
