FROM python:3.10-slim AS build
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy

COPY .. .


FROM python:3.10-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y netcat

COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY .. .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]
