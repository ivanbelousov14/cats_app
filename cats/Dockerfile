FROM python:3.10-slim


#RUN apt-get update && apt-get install -y \
#    curl \
#    && curl -sSL https://install.python-poetry.org | python3 - \
#    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev

COPY . .

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
