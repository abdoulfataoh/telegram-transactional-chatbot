# coding: utf-8

from typing import List, Callable

from telegram.ext import Application
from telegram.ext import ApplicationBuilder
from telegram import Bot
from telegram import BotCommand


class TelegramBot:
    _app: ApplicationBuilder
    _bot: Bot

    def __init__(
        self,
        api_token: str,
        handlers: List[Callable[[Application], None]]
    ):
        self._app = ApplicationBuilder().token(api_token).build()
        self._bot = self._app.bot
        self.add_handlers(handlers)
 
    def add_handlers(self, handlers: List[Callable[[Application], None]]):
        for handler in handlers:
            handler(self._app)

    def run(self) -> None:
        self._app.run_polling()
