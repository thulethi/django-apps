FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add build-base gcc libpq musl-dev python3-dev postgresql-dev

RUN mkdir /app
WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip3 install --upgrade pip
# RUN pip3 install virtualenv
# RUN virtualenv venv
# RUN . venv/bin/activate && pip3 install -r requirements.txt

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Image built, but not found Django
# COPY Pipfile.lock Pipfile.lock
# RUN pip install pipenv
# RUN pipenv install

# Image built, but DB connection refused
# COPY Pipfile Pipfile.lock /app/
# RUN pip install pipenv && pipenv install --system

COPY . app/

EXPOSE 8000

# CMD ["pipenv", "run", "python", "./mysite/manage.py runserver 0.0.0.0:8000"]
