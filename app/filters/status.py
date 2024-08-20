from aiogram.filters import Filter
from aiogram.types import Message


class AdminFilter(Filter):
    def __init__(self, super: bool = False):
        self.super = super

    async def __call__(self, message: Message, **data) -> bool:
        user = data['user']
        _is = user.is_admin(self.super)
        return _is