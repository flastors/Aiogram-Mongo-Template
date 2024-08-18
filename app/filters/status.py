from aiogram.filters import Filter
from aiogram.types import Message
from data.config import OWNER

class AdminFilter(Filter):

    async def __call__(self, message: Message) -> bool:
        return str(message.from_user.id) == OWNER