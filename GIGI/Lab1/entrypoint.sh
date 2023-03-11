#!/bin/sh

#if [ "$POSTGRES_DATABASE" = "postgres" ]
#then
#    echo "Waiting for postgres..."
#
#    while ! nc -z $HOST $PORT; do
#      sleep 0.1
#    done
#
#    echo "PostgreSQL started"
#fi
#
#echo "Waiting for rabbitmq..."
#
#while ! nc -z $RABBITMQ_HOST $RABBITMQ_PORT; do
#  echo $RABBITMQ_HOST $RABBITMQ_PORT
#  echo "Waiting for rabbitmq..."
#  sleep 0.1
#done
#
#echo "Rabbitmq started"

echo "start entrypoint"

python3 main.py
#python3 manage.py runserver 0.0.0.0:8000

exec "$@"
