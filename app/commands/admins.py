from aiogram.types import BotCommand, BotCommandScopeChat

from loader import bot
from .users import get_default_commands


def get_admins_commands():
    commands = get_default_commands()
    commands.extend([
        BotCommand(command='/admin', description='admin menu')
    ])
    return commands


async def set_admins_commands(id: int):
    await bot.set_my_commands(get_admins_commands(), scope=BotCommandScopeChat(chat_id=id))