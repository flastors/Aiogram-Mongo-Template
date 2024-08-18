from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from data.config import TELEGRAM_BOT_TOKEN, RD_URI

bot = Bot(TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode='html'))

if RD_URI:
    from aiogram.fsm.storage.redis import RedisStorage
    from redis.asyncio.client import Redis

    storage = RedisStorage(Redis.from_url(RD_URI))
else:
    from aiogram.fsm.storage.memory import MemoryStorage

    storage = MemoryStorage()

dp = Dispatcher(storage=storage, bot=bot)