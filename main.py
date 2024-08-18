import asyncio

from loader import bot, dp

from app.commands import set_default_commands, set_admins_commands
from app.handlers import setup_handlers
from app.middlewares import setup_middlewares

from utils import logger

from data.config import OWNER

async def on_startup() -> None:
    await set_default_commands()
    await set_admins_commands(OWNER)
    logger.info('Bot started!')

async def on_shutdown() -> None:
    logger.info('Bot stopped!')

async def main() -> None:
    setup_middlewares(dp)
    setup_handlers(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())