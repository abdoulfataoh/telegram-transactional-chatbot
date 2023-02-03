# coding: utf-8

from app import settings
from app.telegram import handlers
from app.telegram import TelegramBot


__all__ = [
    'telegram_bot',
 ]

# [Prod Handlers]
used_handlers = [
    handlers.health_handler,
    handlers.hello_handler,
    handlers.conversation_handler,
]

telegram_bot = TelegramBot(
    api_token=settings.BOT_API_TOKEN,  # type: ignore
    handlers=used_handlers,  # type: ignore
)
