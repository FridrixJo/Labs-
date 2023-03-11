FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBITECODE 1

RUN apt-get update

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY . .

#CMD ["python3", "main.py"]

#COPY entrypoint.sh .

RUN chmod a+x ./entrypoint.sh

ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]
