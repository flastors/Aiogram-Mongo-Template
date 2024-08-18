from aiogram.types import Message
from aiogram.filters import Command

from ..routers import user_router as router

@router.message(Command('start'))
async def _start(message: Message):
    await message.answer('Hello, I\'m bot')

@router.message()
async def _echo(message: Message):
    await message.reply(message.text)