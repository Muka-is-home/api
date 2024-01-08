web: gunicorn app.wsgi
release: python manage.py makemigration
release: python manage.py migrate
python manage.py loaddata user_types tags states specializations content_types
