# coding: utf-8

import logging

from environs import Env
from uuid import uuid4


logging.basicConfig(level=logging.DEBUG)

env = Env()

# [Bot General Config]
BOT_NAME = env.str('BOT_NAME', 'Bot Name')
BOT_DESCRIPTION = env.str('BOT_DESCRIPTION', 'Bot Description')
BOT_API_TOKEN = env.str('BOT_API_TOKEN', 'THE BOT API TOKEN')

# [Support Operators]
BOT_MAIN_MENU = env.list(
  'BOT_TASKS',
  [
    ['↑ Deposit', '↓ Withdrawal'],
    ['? Q&A', '📱 Contact us'],
    ['Back', 'Home']
  ]
)
DEPOSIT_OPERATORS = env.list(
  'DEPOSIT_OPERATORS',
  [
    ['Orange Money', 'Mouv Money'],
    ['Wave', 'Yup'],
    ['Back', 'Home']
  ]
)

# [MESSAGES]
HOME_MESSAGE = env.str(
                'HOME_MESSAGE',
                'Hey 🤚 {first_name}, \n'
                'we are delighted to see you again. \n'
                'What can we do for you ? \n\n'
                'today is: {date}'
)

# [Handlers UUID]
HEALTH_ID = env.uuid('HEALTH', uuid4())
HELLO_ID = env.uuid('HELLO', uuid4())
START_ID = env.uuid('START', uuid4())
GOODBYE_ID = env.uuid('GOODBYE', uuid4())
CHOOSE_TASK_ID = env.uuid('CHOOSE_TASK', uuid4())
CHOOSE_DEPOSIT_OPERATOR_ID = env.uuid('CHOOSE_DEPOSIT_OPERATOR', uuid4())
