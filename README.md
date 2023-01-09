# Telegram Transactionl Chatbot

In this project, we proposed a  transactional `telegram chatbot` for exchanging money between mobile money operators and other digital currencies.

![cover](https://github.com/abdoulfataoh/telegram-transactional-chatbot/blob/master/docs/cover.jpg)

## Create a new telegram bot
1. Fist, search @botfarther on telegram to create a bot.
2. Request @botfather for the new bot access management token

## Config

1. Install poetry for virtual env management if it not already done
```bash
sudo apt-get update
sudo apt-get install poetry
```

2. Install projet dependencies
from projet root folder type
```bash
poetry installl
```

3. Enable virtual env
```bash
poetry shell
```

4. Export bot access token
```bash
export BOT_API_TOKEN='access management token'
```

##  Start the project
```bash
python3 start.py
```
## Start the project with Docker

1. skip steps 1, 2, 3 of config section
2. launch project with docker-compose
```python
docker-compose up
```

## How to add a Message Handler

A handler is an update event: for example a new text incoming message, a new voice incoming message, etc.
The list below enumerate some message handlers:

- [telegram.ext.CommandHandler](https://docs.python-telegram-bot.org/en/stable/telegram.ext.commandhandler.html)
- [telegram.ext.ConversationHandler](https://docs.python-telegram-bot.org/en/stable/telegram.ext.conversationhandler.html)
- [telegram.ext.MessageHandler](https://docs.python-telegram-bot.org/en/stable/telegram.ext.messagehandler.html)
- [telegram.ext.PollAnswerHandler](https://docs.python-telegram-bot.org/en/stable/telegram.ext.pollanswerhandler.html)

For the complete list see this [link](https://docs.python-telegram-bot.org/en/stable/telegram.ext.html)

1. add a new function on this [app/telegram/handlers.py](https://github.com/abdoulfataoh/telegram-transactional-chatbot/blob/master/app/telegram/handlers.py) module

that function must have one parameter to take an Application object.
the code below is an example to add to add `CommandHandler`

```python

# app/telegram/handlers.py

from telegram.ext import CommandHandler
from telegram.ext import Application


def new_command_handler(app: Application) -> None
    handler = CommandHandler(command='health', callback=callback)
    app.add_handler(handler)
    
```