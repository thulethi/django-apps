FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add build-base gcc libpq musl-dev python3-dev postgresql-dev

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . app/

EXPOSE 8000
