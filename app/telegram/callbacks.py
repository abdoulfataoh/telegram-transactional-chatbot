# coding: utf-8

import logging

from telegram import Update
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import ContextTypes

from app import settings

logger = logging.getLogger(__name__)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello ✋ {update.effective_user.first_name}')


async def choose_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = settings.BOT_TASKS
    await update.message.reply_text(
        text='Please choose a task in the below list',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder='Select a Task'
        )
    )


async def choose_deposit_operator(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = settings.DEPOSIT_OPERATORS
    await update.message.reply_text(
        text='Select choose an Operator for your deposit',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder='Select an Operator'
        )
    )
