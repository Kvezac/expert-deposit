# pull the official docker image
FROM python:3.11-slim

WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry add uvicorn
RUN poetry install


COPY . ./app


EXPOSE 8000

CMD ["uvicorn", "main:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000", "--reload"]