from aiogram import Dispatcher

from .user import UserMiddleware

def setup_middlewares(dp: Dispatcher) -> None:
    dp.update.middleware(UserMiddleware())
