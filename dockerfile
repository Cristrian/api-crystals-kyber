FROM python:3.11-alpine

RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /app

# install poetry dependencies
COPY poetry.lock pyproject.toml ./
COPY . .

RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root

CMD ["python3", "main.py"]