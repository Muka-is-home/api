web: gunicorn app.wsgi
release: python manage.py makemigration
release: python manage.py migrate
release: python manage.py loaddata user_types tags states counties specializations content_types

