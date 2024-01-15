# Project Directions

## Running the app

- **To run locally**, just run the commands below

## Install dependencies

- Make a copy of the `.env.sample` in the root directory and name it `.env`

Install pipenv if you do not currently have it. This will allow you to install the version of python this project is using.

```shell
pipenv shell
pipenv install
```

- Create a secret key for the .env 

```shell
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Run migration

This will create a local db

```shell
python3 manage.py migrate
```

## Start the server

```shell
python3 manage.py runserver
```

## If there are any code updates

```shell
python3 manage.py migrate
```

## Login to the admin

Create a local super user

```shell
python3 manage.py createsuperuser --email admin@gmail.com --username admin
```

enter your password for the NEW SUPER USER twice

To login navigate to: <http://127.0.0.1:8000/muka/login>

## If you get errors
- make sure that you are in the shell environment
