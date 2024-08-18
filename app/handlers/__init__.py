from aiogram import Dispatcher

from app.filters import AdminFilter

from .admins import router as admin_router
from .users import router as user_router

def setup_handlers(dp: Dispatcher) -> None:
    admin_router.message.filter(AdminFilter())
    dp.include_routers(admin_router, user_router)