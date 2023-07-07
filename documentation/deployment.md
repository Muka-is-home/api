# Deployment

## How to deploy QA

- Make sure you're in the root directory
- Run this script:

    ```python
    python scripts/heroku-deploy.py qa
    ```

- It may ask you to login into heroku, do so.
- It will then update env variables if needed in heroku
- It will ask you to make sure you want to deploy the branch you're on
  - If you're sure select "Y"
