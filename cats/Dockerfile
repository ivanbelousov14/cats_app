FROM python:3.10-slim


# Установите зависимости системы
RUN apt-get update && apt-get install -y \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы конфигурации Poetry
COPY pyproject.toml poetry.lock ./

# Установите зависимости с помощью Poetry
RUN poetry install --no-root --no-dev

# Скопируйте остальной код приложения
COPY . .

# Команда для запуска вашего приложения
CMD ["poetry", "run", "python", "manage.py", "runserver", "127.0.0.1:8000"]



#WORKDIR /code
#
#RUN pip install poetry
#
#COPY pyproject.toml poetry.lock /code/
#COPY requirements.txt .
#
#RUN poetry install --no-interaction --no-ansi
#
#COPY authentication .
#COPY cats_show .
#COPY manage.py .
#
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#
##LABEL authors="ivan"
##
##ENTRYPOINT ["top", "-b"]