from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from motor.motor_tornado import MotorClient 

from data.config import (MONGO_NAME, MONGO_URL, RD_URI,
                         TELEGRAM_BOT_TOKEN)

bot = Bot(TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode='html'))

if RD_URI:
    from aiogram.fsm.storage.redis import RedisStorage
    from redis.asyncio.client import Redis

    storage = RedisStorage(Redis.from_url(RD_URI))
else:
    from aiogram.fsm.storage.memory import MemoryStorage

    storage = MemoryStorage()

dp = Dispatcher(storage=storage, bot=bot)
client = MotorClient(MONGO_URL)
db = client[MONGO_NAME]
