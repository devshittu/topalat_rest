# pull official base image
#FROM python:3.8.3-alpine
#FROM python:3
FROM python:3.7-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## install psycopg2 dependencies
#RUN apk update && apk add  --no-cache --virtual .build-deps \
#    postgresql-dev gcc python3-dev musl-dev \
#    && pip install --no-cache-dir psycopg2 \
#    && apk del --no-cache .build-deps
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN pip install -r requirements.txt
# Uncomment after creating your docker-entrypoint.sh
#COPY ./entrypoint.sh /

#ENTRYPOINT ["./entrypoint.sh"]
# copy project
COPY . .