# coding: utf-8

from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram.ext import ConversationHandler
from telegram.ext import MessageHandler
from telegram.ext import filters

from app import settings
from app.telegram import callbacks


def health_handler(app: Application) -> None:
    app.add_handler(
        CommandHandler(
            command='health',
            callback=callbacks.health
        )
    )


def hello_handler(app: Application) -> None:
    app.add_handler(
        CommandHandler(
            command='hello',
            callback=callbacks.hello
        )
    )


def conversation_handler(app: Application) -> None:
    conver_handler = ConversationHandler(
        entry_points=[CommandHandler('start', callbacks.choose_task)],
        states={
            settings.CHOOSE_DEPOSIT_OPERATOR_ID : [
                MessageHandler(
                    filters.TEXT,
                    callbacks.choose_deposit_operator
                )
               ]
        },
        fallbacks=[]
    )
    app.add_handler(conver_handler)
