from aiogram.types import BotCommand, BotCommandScopeDefault

from loader import bot

def get_default_commands():
    commands = [
        BotCommand(command='/start', description='start chatting')
    ]
    
    return commands


async def set_default_commands():
    await bot.set_my_commands(get_default_commands(), scope=BotCommandScopeDefault())
