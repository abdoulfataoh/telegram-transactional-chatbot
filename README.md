# Telegram Transactionl Chatbot

In this project, we proposed a  transactional `telegram chatbot` for exchanging money between mobile money operators and other digital currencies.

## Create a new telegram bot
1. Fist, search @botfarther on telegram to create a bot.
2. Request @botfather for the new bot access management token

# Config

- Host running
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

5. Start the project
```bash
python3 start.py
```

- Container running
```python
docker-compose up
```
 