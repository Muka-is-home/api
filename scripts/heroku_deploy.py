import os
import sys

from git import Repo


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# pylint: disable=wrong-import-position
from scripts.env_variables import env_vars  # noqa
# pylint: enable=wrong-import-position

DEPLOY_DIR = "../"

GIT_RELATIVE_PATH = "../"


def has_tool(name):
    """Check whether `name` is on PATH and marked as executable."""

    from shutil import which

    return which(name) is not None


if __name__ == "__main__":
    # Check to see if user has Heroku CLI installed

    has_heroku = has_tool("heroku")
    app = env_vars["QA_APP_NAME"] if "qa" in sys.argv else env_vars["PROD_APP_NAME"]

    if not has_heroku:
        print("You need access to the Heroku CLI to use this script")
        print("Instructions are here: \
        https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli")  # noqa: E501
    else:
        path = os.getcwd()
        path_split = path.split("/")
        backend_index = path_split.index(DEPLOY_DIR)
        backend_index = path_split.index(DEPLOY_DIR)
        last_index = len(path_split) - 1

        if last_index != backend_index:
            BACKEND_PATH = "/".join(path_split[0:(backend_index + 1)])
            os.chdir(BACKEND_PATH)

        repo = Repo(GIT_RELATIVE_PATH)
        if env_vars["PROD_APP_NAME"] not in repo.remotes:
            repo.create_remote(
                env_vars["PROD_APP_NAME"], env_vars["PROD_GIT_REPO"])

        if env_vars["QA_APP_NAME"] not in repo.remotes:
            repo.create_remote(
                env_vars["QA_APP_NAME"], env_vars["QA_GIT_REPO"])

        dependencies_installed = [
            os.popen("pip freeze | grep whitenoise").read(),
            os.popen("pip freeze | grep dj-database-url").read(),
            os.popen("pip freeze | grep psycopg2-binary").read(),
            os.popen("pip freeze | grep gunicorn").read()
        ]

        if "" in dependencies_installed:
            os.system(
                "pipenv install \
                    whitenoise \
                    dj_database_url \
                    psycopg2-binary \
                    gunicorn")

        has_all_variables = False not in [
            os.popen(
                f"heroku config:get IS_HEROKU  --app {app}").read() != "\n",
            os.popen(
                f"heroku config:get API_HOST  --app {app}").read() != "\n",
            os.popen(
                f"heroku config:get FRONTEND_ORIGIN  --app {app}").read() != "\n",
            os.popen(
                f"heroku config:get SECRET_KEY  --app {app}").read() != "\n"
        ]

        if not has_all_variables:
            os.system(
                "heroku config:set IS_HEROKU=True  --app {app}")
            os.system(
                f"heroku config:set SECRET_KEY={env_vars['SECRET_KEY']} --app {app}")
            os.system(
                f"heroku config:set FRONTEND_ORIGIN={env_vars['HEROKU_FRONTEND_ORIGIN']} --app {app}")
            HOST_URL = env_vars["HEROKU_API_HOST_QA"] if app == env_vars["QA_APP_NAME"] else env_vars["HEROKU_API_HOST"]
            os.system(f"heroku config:set API_HOST={HOST_URL} --app {app}")
            os.system(f"heroku config  --app {app}")

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
            os.chdir(GIT_RELATIVE_PATH)
            os.system(
                f"git push --force {app} `git subtree split \
                    --prefix {DEPLOY_DIR} {active_branch}`:refs/heads/main")
