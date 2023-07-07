import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# pylint: disable=wrong-import-position
from scripts.env_variables import env_vars  # noqa
# pylint: enable=wrong-import-position


def create_superuser(_, app):
    os.system(
        f"heroku run python manage.py createsuperuser \
            --email {['SUPER_USER_EMAIL']} --username {env_vars['SUPER_USER_USERNAME']}  --app {app}")


def migrate_db(_, app):
    os.system(f"heroku run python manage.py migrate --app {app}")


def makemigrations_db(_, app):
    os.system(
        f"heroku run python manage.py makemigrations --app {app}")


def help_text(command_map, app):
    print(f"Available subcommands for {app} app:")
    for key in command_map:
        print(f"- {key}")


if __name__ == "__main__":
    ARGUMENT = ""
    COMMAND_MAP = {
        "migrate": migrate_db,
        "makemigrations": makemigrations_db,
        "createsuperuser": create_superuser,
        "help": help_text
    }
    COMMAND = COMMAND_MAP["help"]

    try:
        COMMAND_ARG = sys.argv[1]
        app_name = env_vars["QA_APP_NAME"] if "qa" in sys.argv else env_vars["PROD_APP_NAME"]
        COMMAND = COMMAND_MAP[COMMAND_ARG]
    except KeyError:
        print(f"Unknown command: '{ARGUMENT}'")
        print("Type 'heroku-commands.py help' for usage.")
    else:
        COMMAND(COMMAND_MAP, app_name)
