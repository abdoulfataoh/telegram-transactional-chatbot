# coding: utf-8

import logging

from environs import Env

from app.telegram import handlers

logging.basicConfig(level=logging.DEBUG)

env = Env()

# [Bot General Config]
BOT_NAME = env.str('BOT_NAME', 'Bot Name')
BOT_DESCRIPTION = env.str('BOT_DESCRIPTION', 'Bot Description')
BOT_API_TOKEN = env.str('BOT_API_TOKEN', '5929760713:AAFtqwwKzcSAXpy5YYlVTyta56fKuiueWYY')

# [Support Operators]
BOT_TASKS = env.list('BOT_TASKS', [['↑ Deposit', '↓ Withdrawal'], ['? Q&A', '📱 Contact us']])
DEPOSIT_OPERATORS = env.list('DEPOSIT_OPERATORS', [['Orange Money', 'Mouv Money'], ['Wave', 'Yup']])

# [Handlers config]
HANDLERS = env.list(
  'HANDLERS',
  [
    handlers.hello_handler,
    handlers.choose_task_handler,
    handlers.choose_deposit_operator_handler,
  ]
)
