# coding: utf-8

from telegram.ext import Application
from telegram.ext import CommandHandler

from app.telegram import callbacks

def hello_handler(app: Application) -> None:
    app.add_handler(
        CommandHandler(
            command='hello',
            callback=callbacks.hello
        )
    )


