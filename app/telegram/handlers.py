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


def choose_task_handler(app: Application) -> None:
    app.add_handler(
        CommandHandler(
            command='task',
            callback=callbacks.choose_task
        )
    )


def choose_deposit_operator_handler(app: Application) -> None:
    app.add_handler(
        CommandHandler(
            command='operator',
            callback=callbacks.choose_deposit_operator
        )
    )
