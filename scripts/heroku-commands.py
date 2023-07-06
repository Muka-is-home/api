import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from scripts.env_variables import env_vars  # noqa


def create_superuser(_, app):
    os.system(
        "heroku run python manage.py createsuperuser \
            --email {0} --username {1}  --app {2}".format(['SUPER_USER_EMAIL'], env_vars['SUPER_USER_USERNAME'], app))


def migrate_db(_, app):
    os.system("heroku run python manage.py migrate --app {0}".format(app))


def makemigrations_db(_, app):
    os.system(
        "heroku run python manage.py makemigrations --app {0}".format(app))


def help_text(command_map, app):
    print("Available subcommands for {0} app:".format(app))
    for key in command_map:
        print("- {0}".format(key))


if __name__ == "__main__":
    argument = ''
    command = None

    COMMAND_MAP = {
        "migrate": migrate_db,
        "makemigrations": makemigrations_db,
        "createsuperuser": create_superuser,
        "help": help_text
    }

    try:
        command_arg = sys.argv[1]
        app = env_vars['QA_APP_NAME'] if "qa" in sys.argv else env_vars['PROD_APP_NAME']
        command = COMMAND_MAP[command_arg]
    except KeyError:
        print("Unknown command: '{0}'".format(argument))
        print("Type 'heroku-commands.py help' for usage.")
    else:
        command(COMMAND_MAP, app)
