# django-polls-app

Polls Application is a web-based polls written in Django.

## Stack
- Python 3.8
- Django 3.0.8
- PostgreSQL 12.3

## Development
- Make sure to have `python` and `pip` installed
- Install PipEnv
```
pip install --user pipenv
```

- Activate a virual environment using `pipenv`
```
pipenv shell
```
- Install required packages with dev dependencies
```
pipenv install -r requirements.txt
```
- Create `.env` file and fill in `SECRET_KEY`
- Start the development server inside the same directory with manage.py
```
python manage.py runserver

```
- Visit http://127.0.0.1:8000/admin/ to create a poll.
- Visit http://127.0.0.1:8000/polls/ to participate in the poll.

## Unit tests
Run tests
```
python manage.py test polls
```
