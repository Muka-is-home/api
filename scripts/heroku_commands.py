import os
import sys

from utils import get_env

env = get_env(__file__)


def create_superuser():
    os.system(
        f"heroku run python manage.py createsuperuser \
            --email {env('SUPER_USER_EMAIL')} --username {env('SUPER_USER_USERNAME')}"
    )


def migrate_db():
    os.system("heroku run python manage.py migrate")


def makemigrations_db():
    os.system(
        "heroku run python manage.py makemigrations")


def add_heroku_remotes():
    os.system("heroku git:remote -a muka-staging")


COMMAND_MAP = {
    "migrate": migrate_db,
    "makemigrations": makemigrations_db,
    "createsuperuser": create_superuser,
    "herokuremotes": add_heroku_remotes
}


def help_text(command_map):
    print(f"Available subcommands for {env('HEROKU_STAGING_APP_NAME')} app:")
    for key in command_map:
        print(f"- {key}")


if __name__ == "__main__":
    ARGUMENT = ""
    COMMAND = COMMAND_MAP["help"]

    try:
        COMMAND_ARG = sys.argv[1]
        COMMAND = COMMAND_MAP[COMMAND_ARG]
    except KeyError:
        print(f"Unknown command: '{ARGUMENT}'")
        print("Type 'heroku_commands.py help' for usage.")
    else:
        COMMAND()
