from pathlib import Path

from environs import Env

env = Env()
env.read_env()

DIR = Path(__file__).absolute().parent.parent

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')
OWNER = env.str('OWNER', None)

RD_DB = env.int('RD_DB', None)
RD_HOST = env.str('RD_HOST', None)
RD_PORT = env.int('RD_PORT', None)

RD_URI = env.str('RD_URI', default=None)
if RD_DB and RD_HOST and RD_PORT:
    RD_URI = f'redis://{RD_HOST}:{RD_PORT}/{RD_DB}'