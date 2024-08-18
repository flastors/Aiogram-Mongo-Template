from aiogram.types import Message
from aiogram.filters import Command

from ..routers import admin_router as router

@router.message(Command('admin'))
async def _start(message: Message):
    await message.answer('Hello, my Admin')