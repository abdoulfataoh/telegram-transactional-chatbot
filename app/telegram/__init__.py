# coding: utf-8

from app import settings
from app.telegram.telegram_bot import TelegramBot


telegram_bot = TelegramBot(
    api_token=settings.BOT_API_TOKEN,
    handlers=settings.HANDLERS,
)
