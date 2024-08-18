from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Update

from loader import bot
from database.models import User

class UserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any],
    ) -> Any:
        if event.message:
            from_user = event.message.from_user
        if event.callback_query:
            from_user = event.callback_query.from_user
        if event.inline_query:
            from_user = event.inline_query.from_user

        user = await User.get_or_create(from_user.id, from_user.first_name, from_user.username)
        data['user'] = user
        if user.status != "banned":  
            return await handler(event, data)
        return await bot.send_message(from_user.id, "Вы заблокированы")