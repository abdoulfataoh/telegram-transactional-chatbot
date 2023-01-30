# Coding: utf-8

# [Base image]
FROM python:3.10

# [Meta data]
LABEL name="telegram-transactional-chatbot"
LABEL authors="abdoulfataoh"

# [Wordir]
WORKDIR /src

# [Env variables]
ENV BOT_API_TOKEN=${BOT_API_TOKEN}

# [Source code]
ADD ./ /src

# [Install poetry]
RUN pip install -U pip
RUN pip install poetry

# [Install requiered modules]
RUN poetry config virtualenvs.in-project true
RUN poetry install

# [Enable venv]
ENV PATH="/src/.venv/bin:$PATH"

# # [Start the app]
CMD [ "python3", "start.py" ]
