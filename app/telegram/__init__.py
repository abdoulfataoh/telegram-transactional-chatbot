# coding: utf-8

from app import settings
from app.telegram.bot import TelegramBot
# from app.telegram import handlers

telegram_bot = TelegramBot(
    api_token=settings.BOT_API_TOKEN,
    handlers=settings.HANDLERS,
)
