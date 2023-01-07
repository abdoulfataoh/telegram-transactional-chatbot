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
 