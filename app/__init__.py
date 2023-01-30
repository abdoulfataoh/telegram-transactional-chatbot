# coding: utf-8

from app import settings
from app.telegram.core import TelegramBot
from app.telegram import handlers
from app.telegram import callbacks

__all__ = [
    'telegram_bot',
    'handlers',
    'callbacks',
 ]

telegram_bot = TelegramBot(
    api_token=settings.BOT_API_TOKEN, # type: ignore
    handlers=settings.HANDLERS, # type: ignore
)
