FROM python:3.10-slim as build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy


FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]