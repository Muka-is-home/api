import os

import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(BASE_DIR, '.env'), "asdasdas")

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, ""),
    IS_HEROKU=(bool, False)
)
env.read_env(os.path.join(BASE_DIR, '.env'))

env_vars = {
    'HEROKU_FRONTEND_ORIGIN': env("HEROKU_FRONTEND_ORIGIN"),
    'HEROKU_API_HOST_QA': env("HEROKU_API_HOST_QA"),
    'HEROKU_API_HOST': env('HEROKU_API_HOST'),
    'PROD_APP_NAME': env("PROD_APP_NAME"),
    'PROD_GIT_REPO': env("PROD_GIT_REPO"),
    'QA_GIT_REPO': env("QA_GIT_REPO"),
    'QA_APP_NAME': env("QA_APP_NAME"),
    'SECRET_KEY': env("SECRET_KEY"),
    'SUPER_USER_EMAIL': env("SUPER_USER_EMAIL"),
    'SUPER_USER_USERNAME': env("SUPER_USER_USERNAME"),
}
