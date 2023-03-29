# First stage: build image
FROM python:3.10-slim AS build
WORKDIR /app

# Install pipenv and copy Pipfile/Pipfile.lock
RUN pip install --upgrade pip
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pipenv install --system --deploy

# Copy the rest of the application code
COPY .. .


FROM python:3.10-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y netcat

# Copy the installed dependencies from the previous stage
COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy the rest of the application code
COPY .. .

# Set the entrypoint script as executable
RUN chmod +x entrypoint.sh

# Set the entrypoint script as the default command
ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]
