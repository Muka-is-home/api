import os
import sys

from git.repo import Repo


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# pylint: disable=wrong-import-position
from utils import get_env, get_env_names  # noqa
from scripts.heroku_commands import add_heroku_remotes  # noqa
# pylint: enable=wrong-import-position

env = get_env(__file__)

DEPLOY_DIR = "api"


def has_tool(name):
    """Check whether `name` is on PATH and marked as executable."""

    from shutil import which

    return which(name) is not None


if __name__ == "__main__":
    # Check to see if user has Heroku CLI installed

    has_heroku = has_tool("heroku")

    if not has_heroku:
        print("You need access to the Heroku CLI to use this script")
        print("Instructions are here: \
        https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli")  # noqa: E501
    else:
        path = os.getcwd()
        path_split = path.split("/")
        backend_index = path_split.index(DEPLOY_DIR)
        last_index = len(path_split) - 1

        if last_index != backend_index:
            BACKEND_PATH = "/".join(path_split[0:(backend_index + 1)])
            os.chdir(BACKEND_PATH)

        repo = Repo(os.getcwd())

        if "heroku" not in repo.remotes:
            add_heroku_remotes()

        dependencies_installed = [
            os.popen("pip freeze | grep whitenoise").read(),
            os.popen("pip freeze | grep dj-database-url").read(),
            os.popen("pip freeze | grep psycopg2-binary").read(),
            os.popen("pip freeze | grep gunicorn").read()
        ]

        if "" in dependencies_installed:
            os.system(
                "pipenv install")

        env_var_names = get_env_names()
        for v in env_var_names:
            prod_v = f"PROD_{v}"
            os.system(
                f"heroku config:set {v}={env(prod_v)}")
        os.system("heroku config")

        active_branch = repo.active_branch
        SHOULD_DEPLOY_BRANCH = False
        while True:
            try:
                deploy_branch = input(
                    f"Do you want to deploy the {active_branch} branch? \
                    \n y = Yes \
                    \n n = No \
                    \n")
                if deploy_branch.lower() == "n" \
                        or deploy_branch.lower() == "y":
                    deploy_input_no = deploy_branch.lower() == "n"
                    SHOULD_DEPLOY_BRANCH = False if deploy_input_no else True
                    break
                else:
                    print("Please enter y/n")
            except ValueError:
                print("Invalid")
                continue

        if SHOULD_DEPLOY_BRANCH:
            os.system(
                f"git push --force heroku {active_branch}:main")
