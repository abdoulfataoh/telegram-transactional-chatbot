# coding: utf-8

import logging
from uuid import UUID
from datetime import datetime

from telegram import Update
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram.ext import ContextTypes

from app import settings


logger = logging.getLogger(__name__)


today = datetime.now().strftime('%d/%m/%Y %H:%M:%S')


async def health(update: Update, context: ContextTypes.DEFAULT_TYPE) -> UUID:
    await update.message.reply_text(f'I am healthly 😌')
    return settings.HEALTH_ID


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> UUID:
    await update.message.reply_text(f'Hello ✋ {update.effective_user.first_name}')
    return settings.HELLO_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> UUID:
    await update.message.reply_text(
        settings.HOME_MESSAGE.format(
            first_name=update.effective_user.first_name,
            date=today
        )
    )
    return settings.START_ID


async def goodbye(update: Update, context: ContextTypes.DEFAULT_TYPE) -> UUID:
    await update.message.reply_text(f'Goodbye {update._effective_user.first_name}')
    return settings.GOODBYE_ID


async def choose_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> UUID:
    reply_keyboard = settings.BOT_MAIN_MENU
    await update.message.reply_text(
        '🏠 *Home* 🏠 \n\n'
        'Please choose a task in the below list',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder='Select a Task'
        ),
        parse_mode='MarkdownV2', 
    )
    return settings.CHOOSE_DEPOSIT_OPERATOR_ID
    

async def choose_deposit_operator(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = settings.DEPOSIT_OPERATORS
    await update.message.reply_text(
        'Select choose an Operator for your deposit',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder='Select an Operator'
        ),
        parse_mode='MarkdownV2'
    )
    return settings.CHOOSE_DEPOSIT_OPERATOR_ID
